import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import (Property, CredentialProtocol, RunState,
                                  OptionValue, DisplayOptions)
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
            displayName='Вернуть число или строку',
            name='selector_field',
            type=Property.Type.BOOLEAN,
            description=('Переключатель, влияет на тип возвращаемых данных, '
                         'True-число, False-текст'),
            required=True,
            default=True,
        ),
        Property(
            displayName='Переключатель',
            name='switcher',
            type=Property.Type.BOOLEAN,
            default=False,
        ),
        Property(
            displayName='Поле 1',
            name='field1',
            type=Property.Type.OPTIONS,
            options=[
                OptionValue(
                    name='Значение 1',
                    value='value1',
                    description='Значение 1'
                ),
                OptionValue(
                    name='Значение 2',
                    value='value2',
                    description='Значение 2'
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'switcher': [
                        True,
                    ],
                },
            ),
        ),
        Property(
            displayName='Поле 2',
            name='field2',
            type=Property.Type.OPTIONS,
            options=[
                OptionValue(
                    name='Значение 1',
                    value='value1',
                    description='Значение 1'
                ),
                OptionValue(
                    name='Значение 2',
                    value='value2',
                    description='Значение 2'
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'switcher': [
                        True,
                    ],
                },
            ),
        ),
        Property(
            displayName='EmailField',
            name='email',
            type=Property.Type.EMAIL,
            displayOptions=DisplayOptions(
                show={
                    'field1': [
                        'value1',
                    ],
                    'field2': [
                        'value1'
                    ],
                },
            ),
        ),
        Property(
            displayName='DateTimeField',
            name='date_time',
            type=Property.Type.DATETIME,
            displayOptions=DisplayOptions(
                show={
                    'field1': [
                        'value2',
                    ],
                    'field2': [
                        'value2'
                    ],
                },
            ),
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
            selector = json.node.data.properties['selector_field']
            await json.save_result({
                "result": (result if selector else str(result))
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
