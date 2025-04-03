from src.app.exceptions.SessionNotFoundException import SessionNotFoundException
from src.common.decorators.Singleton import Singleton
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.players.StateEnum import StateEnum


@Singleton
class Storage:
    def __init__(self) -> None:
        self._currentPlayer: Player = Player(name="default", state=StateEnum.INSIDE_MENUS)
        self._currentSession: Session | None = None

    def get_current_player(self) -> Player:
        return self._currentPlayer

    def get_current_session(self) -> Session:
        if self._currentSession is None:
            raise SessionNotFoundException('No session found')
        return self._currentSession

    def get_if_session(self) -> Session | None:
        return self._currentSession

    def set_current_session(self, session: Session) -> None:
        self._currentSession = session
