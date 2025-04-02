from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.domain.core.Rules import Rules
from src.domain.core.Storage import Storage


class RunSession(IRunSessionUseCase):
    def execute(self) -> None:
        session = Storage().get_current_session()
        session.run()
        Storage().set_current_session(session)
