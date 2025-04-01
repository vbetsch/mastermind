from src.app.ports.usecases.ICreateSessionUseCase import ICreateSessionUseCase
from src.domain.core.Game import Game
from src.domain.core.Generator import Generator
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class CreateSession(ICreateSessionUseCase):
    def execute(self, player: Player) -> None:
        new_session: Session = Session(player, Generator().generate_combination())
        player.sessions.save(new_session)
        Game().set_current_session(new_session)
