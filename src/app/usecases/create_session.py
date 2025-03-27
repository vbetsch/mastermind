from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.entities.Player import Player


class CreateSession(ISessionUseCase):
    def __init__(self, player: Player, session_repository: ISessionRepository) -> None:
        self.player: Player = player
        self.session_repository: ISessionRepository = session_repository

    def execute(self) -> None:
        print("Create session...")
        # new_session = Session(self.player, Generator().generate_combination())
        # self.session_repository.create(new_session)
