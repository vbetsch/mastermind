from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.common.abstract.IUseCase import IUseCase
from src.domain.entities.Session import Session


class CreateAGame(IUseCase):
    def __init__(self, session_repository: ISessionRepository) -> None:
        self.session_repository: ISessionRepository = session_repository

    def execute(self) -> None:
        new_session = Session()
        self.session_repository.create(new_session)
