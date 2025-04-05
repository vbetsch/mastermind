from src.app.ports.usecases.session.IEndSession import IEndSession
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class EndSession(IEndSession):
    def execute(self) -> None:
        session: Session = Storage().get_current_session()
        session.close()
        Storage().set_current_session(session)
