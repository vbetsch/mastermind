from src.app.controllers.IController import IController
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.app.presenters.PlayerPresenter import PlayerPresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.data.IData import IData
from src.common.patterns.mediator.IMediator import IMediator


class PlayerController(IController):
    def __init__(self, mediator: IMediator, get_player: IPlayerUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._get_player: IPlayerUseCase = get_player

    def handle(self, message: str, sender: Subscriber, data: IData = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_SESSION.name:
                player = self._get_player.execute()
                self.send(message, PlayerPresenter(player))
