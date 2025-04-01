from src.common.decorators.Singleton import Singleton
from src.domain.entities.Player import Player
from src.domain.values.players.StateEnum import StateEnum


@Singleton
class Game:
    def __init__(self) -> None:
        self.currentPlayer: Player = Player(name="default", state=StateEnum.INSIDE_MENUS)

    def get_current_player(self) -> Player:
        return self.currentPlayer
