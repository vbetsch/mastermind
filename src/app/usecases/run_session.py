from src.app.exceptions.SessionNotFoundException import SessionNotFoundException
from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class RunSession(IRunSessionUseCase):
    def execute(self) -> None:
        session: Session | None = Storage().get_current_session()
        if session is None:
            raise SessionNotFoundException('No session found')
        session.run()
        Storage().set_current_session(session)
