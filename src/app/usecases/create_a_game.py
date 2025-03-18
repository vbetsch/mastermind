from src.app.ports.IRepository import IRepository
from src.app.ports.IUseCase import IUseCase
from src.infra.repositories.SessionRepository import SessionRepository


class CreateAGame(IUseCase):
    def __init__(self) -> None:
        self.session_repository: IRepository = SessionRepository()

    def execute(self) -> None:
        self.session_repository.create()
