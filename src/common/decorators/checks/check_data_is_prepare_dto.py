from functools import wraps

from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.exceptions.CallbackException import CallbackException


def check_data_is_prepare_dto(func):
    @wraps(func)
    def wrapper(self, message, sender, data=None):
        if not data or not isinstance(data, PrepareDTO):
            raise CallbackException("Callback prepare doesn't have data")
        return func(self, message, sender, data)
    return wrapper
