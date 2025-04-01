from src.app.controllers.IController import IController
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator
from src.domain.core.Game import Game


class SessionController(IController):
    def __init__(self, mediator: IMediator,
                 create_session: ISessionUseCase,
                 run_session: ISessionUseCase,
                 stop_session: ISessionUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_session: ISessionUseCase = create_session
        self.run_session: ISessionUseCase = run_session
        self.stop_session: ISessionUseCase = stop_session

    def handle(self, message: str, sender: Subscriber) -> None:
        player = Game().get_current_player()

        match message:
                case EventEnum.CREATE_AND_RUN_SESSION.name:
                    self.create_session.execute(player)
                    self.run_session.execute(player)
                case EventEnum.STOP_SESSION.name:
                    self.stop_session.execute(player)
