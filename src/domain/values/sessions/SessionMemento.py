from src.domain.entities.Session import Session
from src.libs.abstract.Memento import Memento


class SessionMemento(Memento):
    def __init__(self, state: Session) -> None:
        self._state = state

    def get_saved_state(self) -> Session:
        return self._state
