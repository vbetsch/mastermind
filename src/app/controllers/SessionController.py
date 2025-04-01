from src.app.controllers.IController import IController
from src.app.ports.usecases.ICreateSessionUseCase import ICreateSessionUseCase
from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.app.ports.usecases.IStopSessionUseCase import IStopSessionUseCase
from src.common.communication.Data import Data
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator


class SessionController(IController):
    def __init__(self, mediator: IMediator,
                 create_session: ICreateSessionUseCase,
                 run_session: IRunSessionUseCase,
                 stop_session: IStopSessionUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_session: ICreateSessionUseCase = create_session
        self.run_session: IRunSessionUseCase = run_session
        self.stop_session: IStopSessionUseCase = stop_session

    def handle(self, message: str, sender: Subscriber, data: Data | None = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_SESSION.name:
                if not data or not data.player:
                    return
                self.create_session.execute(data.player)
                self.run_session.execute()
            case EventEnum.STOP_SESSION.name:
                self.stop_session.execute()
