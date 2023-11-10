import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = 'a0ff2aa1-f609-42d1-8ac0-dbf893750063'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'Skrynnik_Test'
    is_public: bool = False
    displayName: str = 'Skrynnik_Test'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'This is test description'
    properties: List[Property] = [
        Property(
            displayName='Текстовое поле',
            name='text_field',
            type=Property.Type.STRING,
            description='Текстовое поле',
            required=True,
        ),
        Property(
            displayName='Числовое поле',
            name='number_field',
            type=Property.Type.NUMBER,
            description='Числовое поле',
            required=True,
        ),
        Property(
            displayName='Переключатель',
            name='switcher_field',
            type=Property.Type.BOOLEAN,
            description=('Переключатель, влияет на тип возвращаемых данных, '
                         'True-число, False-текст'),
            required=True,
            default=True,
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_field = json.node.data.properties['text_field']
            number_field = json.node.data.properties['number_field']
            result = number_field + int(text_field)
            switcher = json.node.data.properties['switcher_field']
            await json.save_result({
                "result": (result if switcher else str(result))
            })
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
