from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.domain.core.Game import Game


class RunSession(IRunSessionUseCase):
    def execute(self, arg=None) -> None:
        session = Game().get_current_session()
        session.run()

        if Game().get_save_when_played() is True:
            session.save()

        Game().set_current_session(session)
