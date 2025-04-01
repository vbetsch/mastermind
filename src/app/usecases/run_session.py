from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.players.StateEnum import StateEnum


class RunSession(ISessionUseCase):
    def __init__(self, player_repository: IPlayerRepository, session_repository: ISessionRepository) -> None:
        self.player_repository: IPlayerRepository = player_repository
        self.session_repository: ISessionRepository = session_repository

    def execute(self, player: Player) -> None:
        player.set_state(StateEnum.PLAYING)
        self.player_repository.update(player)

        actual_session: Session = player.sessions.get_last_session()
        actual_session.run()
        self.session_repository.update(actual_session)
