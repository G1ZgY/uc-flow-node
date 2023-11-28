from enum import Enum


DISK_URL = 'https://cloud-api.yandex.net/v1/disk/resources/'

class Option(str, Enum):
    authorization = 'Authorization'
    resource = 'Resource'


class Resource(str, Enum):
    customer = 'customer'


class Operation(str, Enum):
    get_all_files = 'get_all_files'
    upload = 'upload'


class Parameters(str, Enum):
    limit = 'limit'
    media_type = 'media_type'
    offset = 'offset'
    fields = 'fields'
    preview_size = 'preview_size'
    preview_crop = 'preview_crop'

