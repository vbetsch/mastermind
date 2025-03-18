from src.domain.entities.Score import Score
from src.domain.values.StatusEnum import StatusEnum


class Session:
    def __init__(self, state: StatusEnum) -> None:
        self._state: StatusEnum = state
        self._score: Score = Score()
