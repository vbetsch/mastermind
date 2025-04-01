from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.domain.entities.Player import Player


class PlayerRepository(IPlayerRepository):
    def create(self, player: Player) -> int:
        pass

    def update(self, player: Player) -> None:
        pass
