from src.domain.values.StatusEnum import StatusEnum


class Turn:
    def __init__(self, state: StatusEnum) -> None:
        self._state: StatusEnum = state
