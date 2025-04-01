from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.domain.core.Game import Game
from src.domain.entities.Player import Player


class RunSession(ISessionUseCase):
    def execute(self, player: Player) -> None:
        session = Game().get_current_session()
        session.run()
        Game().set_current_session(session)
