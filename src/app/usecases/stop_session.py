from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class StopSession(ISessionUseCase):
    def __init__(self, player: Player, session_repository: ISessionRepository) -> None:
        self.player: Player = player
        self.session_repository: ISessionRepository = session_repository

    def execute(self) -> None:
        actual_session: Session | None = self.player.sessions.get_last_session()
        if actual_session:
            actual_session.stop()
            self.session_repository.update(actual_session)
