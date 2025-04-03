from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class MainMenuHandler(IHandler):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.NEW_GAME.name:
                self.send(EventEnum.CREATE_AND_RUN_SESSION.name)
                self.send(EventEnum.SHOW_PLAY_MENU.name)
            case EventEnum.QUIT.name:
                self.send(EventEnum.CANCEL.name)
