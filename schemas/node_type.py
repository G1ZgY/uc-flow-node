import ujson
from typing import List, Tuple

from .enums import Operation, Option, Parameters, Resource
from uc_flow_schemas import flow
from uc_flow_schemas.flow import (Property, CredentialProtocol, RunState,
                                  OptionValue, DisplayOptions)


class NodeType(flow.NodeType):
    id: str = 'a0ff2aa1-f609-42d1-8ac0-dbf893750063'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'Skrynnik_Test'
    is_public: bool = False
    displayName: str = 'Skrynnik_Test_YDisk'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'This is test description'
    properties: List[Property] = [
        Property(
            displayName='Auth_Token',
            name='token',
            type=Property.Type.STRING,
            required=True,
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            options=[
                OptionValue(
                    name='get_all_files',
                    value=Operation.get_all_files,
                    description=('Плоский список всех файлов'
                                'на Диске в алфавитном порядке.'),
                ),
                OptionValue(
                    name='upload',
                    value=Operation.upload,
                    description='Загрузка файла на диск',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            displayOptions=DisplayOptions(
                show={
                    'operation': [
                        Operation.get_all_files,
                    ],
                },
            ),
            options=[
                Property(
                    displayName=Parameters.limit,
                    name=Parameters.limit,
                    type=Property.Type.NUMBER,
                    description=('Количество файлов, описание '
                                 'которых следует вернуть в ответе'),
                    default=20,
                ),
                Property(
                    displayName=Parameters.media_type,
                    name=Parameters.media_type,
                    type=Property.Type.STRING,
                    description=('Тип файлов, которые '
                                 'нужно включить в список')
                ),
                Property(
                    displayName=Parameters.offset,
                    name=Parameters.offset,
                    type=Property.Type.NUMBER,
                    description=('Количество ресурсов с начала списка, '
                                 'которые следует опустить в ответе ')
                ),
                Property(
                    displayName=Parameters.fields,
                    name=Parameters.fields,
                    type=Property.Type.STRING,
                    description=('Список свойств JSON, которые '
                                 'следует включить в ответ.')
                ),
                Property(
                    displayName=Parameters.preview_size,
                    name=Parameters.preview_size,
                    type=Property.Type.STRING,
                    description=('Требуемый размер уменьшенного '
                                 'изображения (превью файла),'),
                ),
                Property(
                    displayName=Parameters.preview_crop,
                    name=Parameters.preview_crop,
                    type=Property.Type.BOOLEAN,
                    description=('Параметр позволяет обрезать превью '
                                 'согласно размеру, заданному в значении '
                                 'параметра preview_size'),
                    default=False
                ),
            ],
        ),
        Property(
            displayName='UploadFile',
            name='upload_file',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'operation': [
                        Operation.upload,
                    ],
                },
            ),
        ),
    ]
