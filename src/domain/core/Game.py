from src.common.decorators.Singleton import Singleton
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.players.StateEnum import StateEnum


@Singleton
class Game:
    def __init__(self) -> None:
        self._dev_mode: bool = False
        self._currentPlayer: Player = Player(name="default", state=StateEnum.INSIDE_MENUS)
        self._currentSession: Session | None = None
        self._save_when_played: bool = False
        self._beads_per_combination: int = 4
        self._max_attempts_before_loose: int = 12

    def get_dev_mode(self) -> bool:
        return self._dev_mode

    def get_current_player(self) -> Player:
        return self._currentPlayer

    def get_current_session(self) -> Session | None:
        return self._currentSession

    def get_save_when_played(self) -> bool:
        return self._save_when_played

    def get_beads_per_combination(self) -> int:
        return self._beads_per_combination

    def get_max_attempts_before_loose(self) -> int:
        return self._max_attempts_before_loose

    def set_current_session(self, session: Session) -> None:
        self._currentSession = session
