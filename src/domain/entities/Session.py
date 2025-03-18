from dataclasses import dataclass, field

from src.domain.entities.Score import Score
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.sessions.SessionMemento import SessionMemento


@dataclass(frozen=True)
class Session:
    status: StatusEnum
    score: Score = field(default_factory=Score)

    def save(self) -> SessionMemento:
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> None:
        session = memento.get_saved_state()
        # TODO: set datas
