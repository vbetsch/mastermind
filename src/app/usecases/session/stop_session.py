from src.app.ports.usecases.session.IStopSessionUseCase import IStopSessionUseCase
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class StopSession(IStopSessionUseCase):
    def execute(self) -> None:
        session: Session | None = Storage().get_if_session()
        if session is not None:
            session.stop()
            Storage().set_current_session(session)
