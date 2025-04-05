from dataclasses import dataclass, replace, field
from typing import Self

from src.common.logs.Logger import Logger
from src.common.patterns.memento.IOriginator import IOriginator
from src.domain.entities.Player import Player
from src.domain.values.combinations.Combination import Combination
from src.domain.values.sessions.SessionMemento import SessionMemento
from src.domain.values.sessions.Turn import Turn
from src.domain.values.stages.StatusEnum import StatusEnum


@dataclass(frozen=False)
class Session(IOriginator):
    player: Player
    secret_combination: Combination
    status: StatusEnum = StatusEnum.NOT_STARTED
    turns: list[Turn] = field(default_factory=list)

    def get_secret_combination(self) -> Combination:
        return self.secret_combination

    def get_previous_proposals(self) -> list[Combination]:
        previous_proposals: list[Combination] = []
        for turn in self.turns:
            proposal: Combination | None = turn.get_if_proposal()
            if proposal:
                previous_proposals.append(proposal)
        return previous_proposals

    def get_previous_proposals_to_string(self) -> list[str]:
        previous_proposals: list[str] = []
        for turn in self.turns:
            proposal: Combination | None = turn.get_if_proposal()
            if proposal:
                previous_proposals.append(str(proposal))
        return previous_proposals

    def add_turn(self, turn: Turn) -> None:
        self.turns.append(turn)

    def run(self) -> None:
        self.status = StatusEnum.RUNNING
        Logger().log("Session started")

    def save(self) -> SessionMemento:
        Logger().log("Session saved")
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session: Self = memento.get_saved_state()
        return replace(self, **vars(session))

    def stop(self) -> None:
        self.status = StatusEnum.STOPPED
        Logger().log("Session stopped", line_break=True)
