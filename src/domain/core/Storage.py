from src.app.exceptions.SessionNotFoundException import SessionNotFoundException
from src.app.exceptions.TurnNotFoundException import TurnNotFoundException
from src.common.decorators.Singleton import Singleton
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.combinations.Combination import Combination
from src.domain.values.players.StateEnum import StateEnum
from src.domain.values.sessions.Turn import Turn


@Singleton
class Storage:
    def __init__(self) -> None:
        self._currentPlayer: Player = Player(name="default", state=StateEnum.INSIDE_MENUS)
        self._currentSession: Session | None = None
        self._currentTurn: Turn | None = None

    def get_current_player(self) -> Player:
        return self._currentPlayer

    def get_current_session(self) -> Session:
        if self._currentSession is None:
            raise SessionNotFoundException('No session found')
        return self._currentSession

    def get_current_secret_combination(self) -> Combination:
        return self.get_current_session().get_secret_combination()

    def get_if_session(self) -> Session | None:
        return self._currentSession

    def set_current_session(self, session: Session) -> None:
        self._currentSession = session

    def get_if_turn(self) -> Turn | None:
        return self._currentTurn

    def get_current_turn(self) -> Turn:
        if self._currentTurn is None:
            raise TurnNotFoundException('No turn found')
        return self._currentTurn

    def set_current_turn(self, turn: Turn) -> None:
        self._currentTurn = turn
