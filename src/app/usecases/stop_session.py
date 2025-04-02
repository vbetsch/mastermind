from src.app.ports.usecases.IStopSessionUseCase import IStopSessionUseCase
from src.domain.core.Game import Game
from src.domain.entities.Session import Session


class StopSession(IStopSessionUseCase):
    def execute(self, arg=None) -> None:
        session: Session | None = Game().get_current_session()
        if session is not None:
            session.stop()
            Game().set_current_session(session)
