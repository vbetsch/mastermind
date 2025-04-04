from src.app.ports.usecases.session.ICreateSessionUseCase import ICreateSessionUseCase
from src.domain.core.Generator import Generator
from src.domain.core.Storage import Storage
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class CreateSession(ICreateSessionUseCase):
    def execute(self, player: Player) -> None:
        new_session: Session = Session(player, Generator().generate_random_combination())
        player.sessions.save(new_session)
        Storage().set_current_session(new_session)
