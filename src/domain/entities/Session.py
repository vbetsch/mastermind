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
    status: StatusEnum = StatusEnum.NOT_STARTED
    score: Score = field(default_factory=Score)
    combination: Combination = Generator().generate_combination()

    def run(self):
        self.status = StatusEnum.RUNNING
        print("Session started")
        while self.status == StatusEnum.RUNNING:
            # TODO: To implement
            print(self.combination)
            print(self.score)
            print("'save' to save the game")
            print("'stop' to save and quit the game")
            print("'quit' to quit the game")
            print("another is a proposal")
            proposal = input("Proposal: ")
            if proposal == "save" or proposal == "stop":
                self.save()
            if proposal == "stop" or proposal == "quit":
                self.status = StatusEnum.STOPPED

    def save(self) -> SessionMemento:
        print("Session saved")
        return SessionMemento(self)

    def restore(self, memento: SessionMemento) -> Self:
        session = memento.get_saved_state()
        return replace(self, **vars(session))
