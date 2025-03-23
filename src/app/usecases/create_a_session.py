from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase
from src.domain.core.Generator import Generator
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class CreateASession(IMainMenuUseCase):
    def __init__(self, player: Player, session_repository: ISessionRepository) -> None:
        self.player: Player = player
        self.session_repository: ISessionRepository = session_repository

    def execute(self) -> None:
        new_session = Session(self.player, Generator().generate_combination())
        self.session_repository.create(new_session)
        new_session.run()
