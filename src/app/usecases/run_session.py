from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.domain.core.Rules import Rules
from src.domain.core.Storage import Storage


class RunSession(IRunSessionUseCase):
    def execute(self, arg=None) -> None:
        session = Storage().get_current_session()
        session.run()

        if Rules().get_save_when_played() is True:
            session.save()

        Storage().set_current_session(session)
