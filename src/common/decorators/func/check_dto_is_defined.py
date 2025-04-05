from functools import wraps
from typing import Type

from src.common.communication.EventEnum import EventEnum
from src.common.exceptions.DTOException import DTOException


def check_dto_is_defined(event: EventEnum, dto_type: Type):
    def decorator(func):
        @wraps(func)
        def wrapper(self, dto=None):
            if not dto or not isinstance(dto, dto_type):
                raise DTOException(f"Event {event.name} doesn't have data")
            return func(self, dto)
        return wrapper
    return decorator
