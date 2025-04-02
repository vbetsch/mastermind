from src.app.ports.usecases.IStopSessionUseCase import IStopSessionUseCase
from src.domain.core.Game import Game


class StopSession(IStopSessionUseCase):
    def execute(self, arg=None) -> None:
        session = Game().get_current_session()
        if session is not None:
            session.stop()
            Game().set_current_session(session)
