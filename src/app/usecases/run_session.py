from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.domain.core.Game import Game


class RunSession(IRunSessionUseCase):
    def execute(self, arg=None) -> None:
        session = Game().get_current_session()
        session.run()
        Game().set_current_session(session)
