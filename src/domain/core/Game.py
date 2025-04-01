from src.common.decorators.Singleton import Singleton
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.players.StateEnum import StateEnum


@Singleton
class Game:
    def __init__(self) -> None:
        self.currentPlayer: Player = Player(name="default", state=StateEnum.INSIDE_MENUS)
        self.currentSession: Session | None = None

    def get_current_player(self) -> Player:
        return self.currentPlayer

    def get_current_session(self) -> Session | None:
        return self.currentSession

    def set_current_session(self, session: Session) -> None:
        self.currentSession = session
