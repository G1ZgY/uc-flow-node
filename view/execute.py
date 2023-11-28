from json import JSONDecodeError
import ujson

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from uc_http_requester.requester import Request

from schemas.enums import DISK_URL, Operation


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
            token = properties['token']
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {token}'
            }
            if properties['operation'] == Operation.get_all_files:
                parameters = get_request_params(properties['parameters'])
                request = Request(
                    url=f'{DISK_URL}files',
                    params=parameters,
                    method=Request.Method.get,
                    headers=headers,
                )
                result = await request.execute()
                await json.save_result({
                    'result': result.json()
                })
                json.state = RunState.complete
            if properties['operation'] == Operation.upload:
                upload_path = properties['upload_file'][0].get('name')
                upload_request = Request(
                    url=f'{DISK_URL}upload',
                    params={'path': upload_path},
                    headers=headers
                )
                upload_request = await upload_request.execute()
                upload_request = upload_request.json()
                upload_url = upload_request['href']
                file_path = properties['upload_file'][0].get('path')
                file_content = Request(
                    url=file_path,
                    method=Request.Method.get,
                )
                file_content = await file_content.execute()
                file_content = file_content.text
                upload = Request(
                    url=upload_url,
                    method=Request.Method.put,
                    data=file_content
                )
                await upload.execute()
                await json.save_result({
                    'result': 'Файл успешно загружен'
                })
                json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
