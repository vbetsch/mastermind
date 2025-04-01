from src.app.controllers.IController import IController
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator


class SessionController(IController):
    def __init__(self, mediator: IMediator,
                 get_player: IPlayerUseCase,
                 create_session: ISessionUseCase,
                 run_session: ISessionUseCase,
                 stop_session: ISessionUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.get_player: IPlayerUseCase = get_player
        self.create_session: ISessionUseCase = create_session
        self.run_session: ISessionUseCase = run_session
        self.stop_session: ISessionUseCase = stop_session

    def handle(self, message: str, sender: Subscriber, data=None) -> None:
        player = self.get_player.execute()

        match message:
                case EventEnum.CREATE_AND_RUN_SESSION.name:
                    self.create_session.execute(player)
                    self.run_session.execute(player)
                case EventEnum.STOP_SESSION.name:
                    self.stop_session.execute(player)
