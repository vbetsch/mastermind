from functools import wraps

from src.common.exceptions.CallbackException import CallbackException


def check_data_fields(func):
    @wraps(func)
    def wrapper(self, message, sender, data=None):
        if (data.all_colors is None
                or data.previous_proposals is None
                or data.beads_per_combination is None):
            raise CallbackException("Callback prepare has data malformed")
        return func(self, message, sender, data)
    return wrapper
