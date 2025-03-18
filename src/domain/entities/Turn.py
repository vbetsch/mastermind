from src.domain.values.StateEnum import StateEnum


class Turn:
    def __init__(self, state: StateEnum) -> None:
        self._state: StateEnum = state
