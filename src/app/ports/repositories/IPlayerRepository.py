from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.entities.Player import Player


class IPlayerRepository(IRepository):
    @abstractmethod
    def find(self, name: str) -> Player | None:
        pass

    @abstractmethod
    def create(self, player: Player, history_id: int) -> int:
        pass

    @abstractmethod
    def update(self, player: Player) -> None:
        pass

    @abstractmethod
    def delete(self, player: Player) -> None:
        pass
