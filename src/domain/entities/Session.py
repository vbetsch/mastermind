from src.domain.values.StateEnum import StateEnum


class Session:
    def __init__(self, state: StateEnum) -> None:
        self._state: StateEnum = state
