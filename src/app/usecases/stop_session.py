from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player


class StopSession(ISessionUseCase):
    def execute(self, player: Player) -> None:
        print("stop session")
