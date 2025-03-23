from dataclasses import dataclass, field, replace
from typing import Self

from src.domain.core.Generator import Generator
from src.domain.entities.Combination import Combination
from src.domain.entities.Player import Player
from src.domain.entities.Score import Score
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.sessions.SessionMemento import SessionMemento


@dataclass(frozen=False)
class Session:
    player: Player
    combination: Combination
    status: StatusEnum = StatusEnum.NOT_STARTED
    score: Score = field(default_factory=Score)

    def run(self):
        self.status = StatusEnum.RUNNING
        print("Session started")

    def save(self) -> SessionMemento:
        print("Session saved")
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session = memento.get_saved_state()
        return replace(self, **vars(session))
