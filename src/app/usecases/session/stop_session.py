from src.app.ports.usecases.session.IStopSessionUseCase import IStopSessionUseCase
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.stages.StatusEnum import StatusEnum


class StopSession(IStopSessionUseCase):
    def execute(self) -> None:
        session: Session | None = Storage().get_if_session()
        if session is not None and session.status != StatusEnum.STOPPED:
            session.stop()
            Storage().set_current_session(session)
