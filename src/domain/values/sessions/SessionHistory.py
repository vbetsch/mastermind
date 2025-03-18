from src.domain.entities.Session import Session
from src.domain.values.sessions.SessionMemento import SessionMemento


class SessionHistory:
    def __init__(self) -> None:
        self._mementos: list[SessionMemento] = []

    def save(self, session: Session) -> None:
        memento = session.save()
        self._mementos.append(memento)

    def undo(self, session: Session) -> None:
        if len(self._mementos) <= 1:
            raise Exception("No sessions to restore")

        self._mementos.pop()
        last_memento: SessionMemento = self._mementos[-1]
        session.restore(last_memento)
