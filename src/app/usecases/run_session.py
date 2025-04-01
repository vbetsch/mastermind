from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class RunSession(ISessionUseCase):
    def __init__(self, session_repository: ISessionRepository) -> None:
        self.session_repository: ISessionRepository = session_repository

    def execute(self, player: Player) -> None:
        actual_session: Session = player.sessions.get_last_session()
        actual_session.run()
        self.session_repository.update(actual_session)
