from functools import wraps

from src.common.communication.EventEnum import EventEnum
from src.common.exceptions.DTOException import DTOException


def check_dto_required_fields(event: EventEnum, dto_class):
    def decorator(func):
        @wraps(func)
        def wrapper(self, dto=None):
            if not isinstance(dto, dto_class):
                raise DTOException(f"Expected instance of {dto_class.__name__}, got {type(dto).__name__}")

            fields = vars(dto).keys()

            for field in fields:
                if getattr(dto, field, None) is None:
                    raise DTOException(f"Event {event.name} has missing or malformed field: {field}")
            return func(self, dto)

        return wrapper

    return decorator
