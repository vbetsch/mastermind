from dataclasses import dataclass, replace, field
from typing import Self

from src.common.logs.Logger import Logger
from src.common.patterns.memento.IOriginator import IOriginator
from src.domain.core.Rules import Rules
from src.domain.entities.Player import Player
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.sessions.SessionMemento import SessionMemento
from src.domain.values.sessions.Turn import Turn


@dataclass(frozen=False)
class Session(IOriginator):
    player: Player
    secret_combination: Combination
    status: StatusEnum = StatusEnum.NOT_STARTED
    turns: list[Turn] = field(default_factory=list)

    def run(self) -> None:
        self.status = StatusEnum.RUNNING
        if Rules().get_dev_mode() is True:
            Logger().log("Session started")

    def save(self) -> SessionMemento:
        if Rules().get_dev_mode() is True:
            Logger().log("Session saved")
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session: Self = memento.get_saved_state()
        return replace(self, **vars(session))

    def stop(self) -> None:
        self.status = StatusEnum.STOPPED
        if Rules().get_dev_mode() is True:
            Logger().log("Session stopped", line_break=True)
