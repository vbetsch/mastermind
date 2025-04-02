from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.domain.core.Storage import Storage
from src.domain.entities.Player import Player


class GetPlayer(IPlayerUseCase):
    def execute(self) -> Player:
        return Storage().get_current_player()
