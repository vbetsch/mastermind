from functools import wraps
from typing import Type

from src.common.communication.EventEnum import EventEnum
from src.common.exceptions.CallbackException import CallbackException


def check_data_is_defined(event: EventEnum, dto: Type):
    def decorator(func):
        @wraps(func)
        def wrapper(self, message, sender, data=None):
            if not data or not isinstance(data, dto):
                raise CallbackException(f"Event {event.name} doesn't have data")
            return func(self, message, sender, data)
        return wrapper
    return decorator
