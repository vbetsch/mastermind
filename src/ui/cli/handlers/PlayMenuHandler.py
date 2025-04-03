from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.exceptions.CallbackException import CallbackException
from src.common.logs.Logger import Logger
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class PlayMenuHandler(IHandler):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber, data: IDto = None) -> None:
        match message:
            case EventEnum.PLAY.name:
                self.send(EventEnum.PREPARE.name)
            case EventEnum.STOP.name:
                self.send(EventEnum.STOP_SESSION.name)
                self.send(EventEnum.SHOW_MAIN_MENU.name)
            case EventEnum.CALLBACK_PREPARE.name:
                if not data or not isinstance(data, PrepareDTO) or data.all_colors is None or data.previous_proposals is None:
                    raise CallbackException("Callback prepare doesn't have data")
                self.send(EventEnum.ASK_PROPOSAL.name, data)
