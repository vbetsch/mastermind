from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.entities.Player import Player


class IPlayerUseCase(IUseCase):
    @abstractmethod
    def execute(self, arg=None) -> Player:
        pass
