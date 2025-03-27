from src.app.controllers.IController import IController
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator


class SessionController(IController):
    def __init__(self, mediator: IMediator, create_session: ISessionUseCase, run_session: ISessionUseCase):
        super().__init__(self.__class__.__name__, mediator)
        self.create_session: ISessionUseCase = create_session
        self.run_session: ISessionUseCase = run_session

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case "CREATE_AND_RUN_SESSION":
                self.create_session.execute()
                self.run_session.execute()
            case _:
                raise Exception(f"Unknown message: {message}")
