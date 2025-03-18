from src.domain.entities.Score import Score
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.sessions.SessionMemento import SessionMemento


class Session:
    def __init__(self, state: StatusEnum) -> None:
        self._state: StatusEnum = state
        self._score: Score = Score()

    def save(self) -> SessionMemento:
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> None:
        session = memento.get_saved_state()
        self._state = session._state
        self._score = session._score
