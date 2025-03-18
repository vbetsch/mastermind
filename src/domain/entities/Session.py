from dataclasses import dataclass, field, replace
from typing import Self

from src.domain.entities.Score import Score
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.sessions.SessionMemento import SessionMemento


@dataclass(frozen=True)
class Session:
    status: StatusEnum = StatusEnum.NOT_STARTED
    score: Score = field(default_factory=Score)

    def save(self) -> SessionMemento:
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session = memento.get_saved_state()
        return replace(self, **vars(session))
