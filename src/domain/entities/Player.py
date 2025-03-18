from src.domain.entities.Score import Score


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._score: Score = Score()
