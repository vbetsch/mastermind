from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.domain.core.Game import Game
from src.domain.entities.Player import Player


class GetPlayer(IPlayerUseCase):
    def execute(self, arg=None) -> Player:
        return Game().get_current_player()
