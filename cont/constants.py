from enum import Enum


class PhoneType(Enum):
    HOME = 'Home'
    WORK = 'Work'
    FAX = 'Fax'
    OTHER = 'Other'

    @classmethod
    def choice(cls):
        return [(item.name, item.value) for item in cls]
