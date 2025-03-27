from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class RunSession(ISessionUseCase):
    def __init__(self, player: Player, session_repository: ISessionRepository) -> None:
        self.player: Player = player
        self.session_repository: ISessionRepository = session_repository

    def execute(self) -> None:
        actual_session: Session = self.player.sessions.get_last_memento().get_saved_state()
        actual_session.run()
        self.session_repository.update(actual_session)
