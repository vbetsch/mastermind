from src.app.controllers.IController import IController
from src.app.data.PlayerData import PlayerData
from src.app.ports.usecases.player.IPlayerUseCase import IPlayerUseCase
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator


class PlayerController(IController):
    def __init__(self, mediator: IMediator, get_player: IPlayerUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._get_player: IPlayerUseCase = get_player

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_SESSION.name:
                player = self._get_player.execute()
                self.send(message, PlayerData(player))
