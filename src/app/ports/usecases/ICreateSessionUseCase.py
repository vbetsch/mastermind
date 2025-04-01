from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.entities.Player import Player


class ICreateSessionUseCase(IUseCase):
    @abstractmethod
    def execute(self, player: Player) -> None:
        pass
