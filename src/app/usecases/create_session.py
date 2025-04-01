from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.core.Generator import Generator
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class CreateSession(ISessionUseCase):
    def __init__(self, session_repository: ISessionRepository) -> None:
        self.session_repository: ISessionRepository = session_repository

    def execute(self, player: Player) -> None:
        new_session: Session = Session(player, Generator().generate_combination())
        session_id: int = self.session_repository.create(new_session, player.sessions.get_id())
        new_session.id = session_id
        player.sessions.save(new_session)
