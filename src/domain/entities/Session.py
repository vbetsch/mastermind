from dataclasses import dataclass, replace
from typing import Self

from src.domain.entities.Combination import Combination
from src.domain.entities.Player import Player
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.sessions.SessionMemento import SessionMemento


@dataclass(frozen=False)
class Session:
    player: Player
    secret_combination: Combination
    status: StatusEnum = StatusEnum.NOT_STARTED

    def run(self):
        self.status = StatusEnum.RUNNING
        print("Session started")

    def save(self) -> SessionMemento:
        print("Session saved")
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session = memento.get_saved_state()
        return replace(self, **vars(session))
