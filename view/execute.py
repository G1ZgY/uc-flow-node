from json import JSONDecodeError
from typing import List, Union
import ujson

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from uc_http_requester.requester import Request

from .info import InfoView
from schemas.enums import Option, Operation


def get_attr(params, attr):
    obj = params.get(attr)
    return obj[0].get(attr) if obj else None

def get_request_params(parameters: dict) -> dict:
    res_parameters = {}
    if parameters:
        for param in parameters:
            if not parameters[param]:
                continue
            res_parameters[param] = get_attr(parameters, param)
    return res_parameters

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            properties = json.node.data.properties
            option = properties['option']
            if option == Option.authorization:
                hostname = properties['hostname']
                branch = properties['branch']
                email = properties['email']
                api_key = properties['api_key']
                url = f'https://{hostname}/v2api/auth/login'
                data = {'email': email, 'api_key': api_key}
                request = Request(
                    url=url,
                    json=data,
                    method=Request.Method.post,
                )
                result = await request.execute()
                result_data = result.json()
                await json.save_result({
                    "token": result_data['token'],
                    "branch": branch,
                    "hostname": hostname
                })
                json.state = RunState.complete
            if option == Option.resource:
                token = json.node.data.properties['auth_result']['token']
                branch = properties['auth_result']['branch']
                hostname = properties['auth_result']['hostname']
                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-ALFACRM-TOKEN': token
                }
                parameters = json.node.data.properties['parameters']
                parameters = get_request_params(parameters)
                if parameters.get('is_study') is not None:
                    parameters['is_study'] = int(parameters['is_study'])
                operation = properties['operation']
                if operation == Operation.update:
                    id = properties['user_id']
                    url = f'https://{hostname}/v2api/{branch}/customer/{operation}?id={id}'
                else:
                    url = f'https://{hostname}/v2api/{branch}/customer/{operation}'
                request = Request(
                    url=url,
                    json=parameters,
                    method=Request.Method.post,
                    headers=headers
                )
                result = await request.execute()
                await json.save_result({
                    'result': result.json()
                })
                json.state = RunState.complete
                
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
