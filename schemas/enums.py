from enum import Enum


class Option(str, Enum):
    authorization = 'Authorization'
    resource = 'Resource'


class Resource(str, Enum):
    customer = 'customer'


class Operation(str, Enum):
    get = 'index'
    create = 'create'
    update = 'update'


class Parameters(str, Enum):
    id = 'id'
    is_study = 'is_study'
    study_status_id = 'study_status_id'
    name = 'name'
    branch_ids = 'branch_ids'
    gender = 'gender'
    age_from = 'age_from'
    age_to = 'age_to'
    phone = 'phone'
    legal_type = 'legal_type'
    legal_name = 'legal_name'
    company_id = 'company_id'
    lesson_count_from = 'lesson_count_from'
    lesson_count_to = 'lesson_count_to'
    balance_contract_from = 'balance_contract_from'
    balance_contract_to = 'balance_contract_to'
    balance_bonus_from = 'balance_bonus_from'
    balance_bonus_to = 'balance_bonus_to'
    removed = 'removed'
    removed_from = 'removed_from'
    removed_to = 'removed_to'
    level_id = 'level_id'
    assigned_id = 'assigned_id'
    employee_id = 'employee_id'
    lead_source_id = 'lead_source_id'
    lead_status_id = 'lead_status_id'
    color = 'color'
    note = 'note'
    date_from = 'date_from'
    date_to = 'date_to'
    next_lesson_date_from = 'next_lesson_date_from'
    next_lesson_date_to = 'next_lesson_date_to'
    tariff_till_from = 'tariff_till_from'
    tariff_till_to = 'tariff_till_to'
    customer_reject_id = 'customer_reject_id'
    comment = 'comment'
    dob = 'dob'
    withGroups = 'withGroups'
    page = 'page'

