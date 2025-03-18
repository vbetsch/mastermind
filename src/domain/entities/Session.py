from src.domain.entities.Score import Score
from src.domain.values.StateEnum import StateEnum


class Session:
    def __init__(self, state: StateEnum) -> None:
        self._state: StateEnum = state
        self._score: Score = Score()
