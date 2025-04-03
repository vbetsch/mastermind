from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.decorators.checks.check_data_fields import check_data_fields
from src.common.decorators.checks.check_data_is_prepare_dto import check_data_is_prepare_dto
from src.common.exceptions.CallbackException import CallbackException
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
                self._handle_callback_prepare(message, sender, data)

    @check_data_is_prepare_dto
    @check_data_fields
    def _handle_callback_prepare(self, message: str, sender: Subscriber, data: IDto = None) -> None:
        self.send(EventEnum.ASK_PROPOSAL.name, data)
