from src.app.ports.usecases.session.ICreateSessionUseCase import ICreateSessionUseCase
from src.common.logs.Logger import Logger
from src.domain.core.Generator import Generator
from src.domain.core.Rules import Rules
from src.domain.core.Storage import Storage
from src.domain.entities.Player import Player
from src.domain.entities.Session import Session


class CreateSession(ICreateSessionUseCase):
    def execute(self, player: Player) -> None:
        new_session: Session = Session(player, Generator().generate_combination())

        if Rules().get_dev_mode() is True:
            Logger().info(f"The response is {new_session.secret_combination}")

        player.sessions.save(new_session)
        Storage().set_current_session(new_session)
