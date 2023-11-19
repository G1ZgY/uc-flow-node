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
    displayName: str = 'Skrynnik_Test_CRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'This is test description'
    properties: List[Property] = [
        Property(
            displayName='Option',
            name='option',
            type=Property.Type.OPTIONS,
            options=[
                OptionValue(
                    name='Authorization',
                    value=Option.authorization,
                    description='авторизация'
                ),
                OptionValue(
                    name='Resource',
                    value=Option.resource,
                    description='Resource'
                ),
            ],
        ),
        Property(
            displayName='HostName',
            name='hostname',
            required=True,
            default='uiscom.s20.online',
            type=Property.Type.STRING,
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='ID филиала',
            name='branch',
            type=Property.Type.NUMBER,
            required=True,
            default=1,
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='Email',
            name='email',
            type=Property.Type.EMAIL,
            required=True,
            default='vehemop789@weirby.com',
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='ApiKey',
            name='api_key',
            type=Property.Type.STRING,
            required=True,
            default='7acaf091-77b5-11ee-8640-3cecef7ebd64',
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.authorization,
                    ],
                },
            ),
        ),
        Property(
            displayName='AuthResult',
            name='auth_result',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource,
                    ],
                },
            ),
        ),
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Customer',
                    value=Resource.customer,
                )
            ],
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='index',
                    value=Operation.get,
                    description='Чтение списка с фильтрацией и пейджинацией',
                ),
                OptionValue(
                    name='create',
                    value=Operation.create,
                    description='Создание новой модели',
                ),
                OptionValue(
                    name='update',
                    value=Operation.update,
                    description='Изменение свойств модели',
                )
            ],
        ),
        Property(
            displayName='ID',
            name='user_id',
            type=Property.Type.NUMBER,
            description='ID пользователя',
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update
                    ]
                },
            ),
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.get
                    ]
                },
            ),
            options=[
                Property(
                    displayName=Parameters.page,
                    name=Parameters.page,
                    type=Property.Type.NUMBER,
                    default='',
                    description='пейджинация'
                ),
                Property(
                    displayName=Parameters.id,
                    name=Parameters.id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id клиента'
                ),
                Property(
                    displayName=Parameters.is_study,
                    name=Parameters.is_study,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    options=[
                        OptionValue(
                            name='Лид',
                            value=0,
                        ),
                        OptionValue(
                            name='Клиент',
                            value=1
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.name,
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    default='',
                    description='полное имя',
                ),
                Property(
                    displayName=Parameters.branch_ids,
                    name=Parameters.branch_ids,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Массив идентификаторов филлиалов',
                ),
                Property(
                    displayName=Parameters.study_status_id,
                    name=Parameters.study_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Статус обучения (StudyStatus)',
                ),
                Property(
                    displayName='Этап воронки продаж',
                    name=Parameters.lead_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Этап воронки продаж (LeadStatus)',
                ),
                Property(
                    displayName='Источник',
                    name=Parameters.lead_source_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Источник (LeadSource)',
                ),
                Property(
                    displayName='Ответственный менеджер',
                    name=Parameters.assigned_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Ответственный менеджер (User)',
                ),
                Property(
                    displayName='Тип клиента',
                    name=Parameters.legal_type,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='Тип клиента (1 - физ.лицо, 2 - юр.лицо)',
                    options=[
                        OptionValue(
                            name='Физ. лицо',
                            value=1,
                        ),
                        OptionValue(
                            name='Юр. лицо',
                            value=2
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.company_id,
                    name=Parameters.company_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Компания (Company)',
                ),
                Property(
                    displayName='Дата рождения',
                    name=Parameters.dob,
                    type=Property.Type.DATE,
                    default='',
                    description='Дата рождения',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.create
                    ]
                },
            ),
            options=[
                Property(
                    displayName=Parameters.is_study,
                    name=Parameters.is_study,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    options=[
                        OptionValue(
                            name='Лид',
                            value=0,
                        ),
                        OptionValue(
                            name='Клиент',
                            value=1
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.name,
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    default='',
                    description='полное имя',
                ),
                Property(
                    displayName=Parameters.branch_ids,
                    name=Parameters.branch_ids,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Массив идентификаторов филлиалов',
                ),
                Property(
                    displayName=Parameters.study_status_id,
                    name=Parameters.study_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Статус обучения (StudyStatus)',
                ),
                Property(
                    displayName='Источник',
                    name=Parameters.lead_source_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Источник (LeadSource)',
                ),
                Property(
                    displayName='Ответственный менеджер',
                    name=Parameters.assigned_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Ответственный менеджер (User)',
                ),
                Property(
                    displayName='Тип клиента',
                    name=Parameters.legal_type,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='Тип клиента (1 - физ.лицо, 2 - юр.лицо)',
                    options=[
                        OptionValue(
                            name='Физ. лицо',
                            value=1,
                        ),
                        OptionValue(
                            name='Юр. лицо',
                            value=2
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.company_id,
                    name=Parameters.company_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Компания (Company)',
                ),
                Property(
                    displayName='Дата рождения',
                    name=Parameters.dob,
                    type=Property.Type.DATE,
                    default='',
                    description='Дата рождения',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            displayOptions=DisplayOptions(
                show={
                    'option': [
                        Option.resource
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Operation.update
                    ]
                },
            ),
            options=[
                Property(
                    displayName=Parameters.is_study,
                    name=Parameters.is_study,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    options=[
                        OptionValue(
                            name='Лид',
                            value=0,
                        ),
                        OptionValue(
                            name='Клиент',
                            value=1
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.name,
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    default='',
                    description='полное имя',
                ),
                Property(
                    displayName=Parameters.branch_ids,
                    name=Parameters.branch_ids,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Массив идентификаторов филлиалов',
                ),
                Property(
                    displayName=Parameters.study_status_id,
                    name=Parameters.study_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Статус обучения (StudyStatus)',
                ),
                Property(
                    displayName='Этап воронки продаж',
                    name=Parameters.lead_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Этап воронки продаж (LeadStatus)',
                ),
                Property(
                    displayName='Источник',
                    name=Parameters.lead_source_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Источник (LeadSource)',
                ),
                Property(
                    displayName='Ответственный менеджер',
                    name=Parameters.assigned_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Ответственный менеджер (User)',
                ),
                Property(
                    displayName='Тип клиента',
                    name=Parameters.legal_type,
                    type=Property.Type.OPTIONS,
                    default='',
                    description='Тип клиента (1 - физ.лицо, 2 - юр.лицо)',
                    options=[
                        OptionValue(
                            name='Физ. лицо',
                            value=1,
                        ),
                        OptionValue(
                            name='Юр. лицо',
                            value=2
                        ),
                    ],
                ),
                Property(
                    displayName=Parameters.company_id,
                    name=Parameters.company_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='Компания (Company)',
                ),
                Property(
                    displayName='Дата рождения',
                    name=Parameters.dob,
                    type=Property.Type.DATE,
                    default='',
                    description='Дата рождения',
                ),
            ],
        ),
    ]
