from src.common.abstract.IMemento import IMemento
from src.domain.entities.Session import Session


class SessionMemento(IMemento):
    def __init__(self, state: Session) -> None:
        self._state = state

    def get_saved_state(self) -> Session:
        return self._state
