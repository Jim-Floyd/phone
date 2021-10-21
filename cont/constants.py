from collections import namedtuple
from enum import Enum


class PhoneType(Enum):
    HOME = 'Home'
    WORK = 'Work'
    FAX = 'Fax'
    OTHER = 'Other'

    @classmethod
    def choice(cls):
        return [(item.name, item.value) for item in cls]

    @staticmethod
    def process():
        sh = namedtuple('a', 'name value')
        _ = list()
        for item in PhoneType:
            _.append(sh(item.name, item.value))
        return _
