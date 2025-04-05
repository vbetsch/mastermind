from src.app.data.PreviousAttemptsData import PreviousAttemptsData
from src.app.ports.usecases.prepare.IGetPreviousAttempts import IGetPreviousAttempts
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class GetPreviousAttempts(IGetPreviousAttempts):

    def execute(self) -> PreviousAttemptsData:
        session: Session = Storage().get_current_session()
        return PreviousAttemptsData(
            attempts=session.get_previous_attempts()
        )
