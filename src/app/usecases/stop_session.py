from src.app.ports.usecases.IStopSessionUseCase import IStopSessionUseCase
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class StopSession(IStopSessionUseCase):
    def execute(self, arg=None) -> None:
        session: Session | None = Storage().get_current_session()
        if session is not None:
            session.stop()
            Storage().set_current_session(session)
