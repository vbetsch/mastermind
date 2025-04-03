from functools import wraps

from src.common.communication.EventEnum import EventEnum
from src.common.exceptions.DTOException import DTOException


def check_data_required_fields(event: EventEnum, dto_class):
    def decorator(func):
        @wraps(func)
        def wrapper(self, message, sender, data=None):
            if not isinstance(data, dto_class):
                raise DTOException(f"Expected instance of {dto_class.__name__}, got {type(data).__name__}")

            fields = vars(data).keys()

            for field in fields:
                if getattr(data, field, None) is None:
                    raise DTOException(f"Event {event.name} has missing or malformed field: {field}")
            return func(self, message, sender, data)

        return wrapper

    return decorator
