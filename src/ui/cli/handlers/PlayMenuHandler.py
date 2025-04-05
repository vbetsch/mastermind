from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.FeedbackDTO import FeedbackDTO
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.decorators.dto.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.dto.check_dto_required_fields import check_dto_required_fields
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class PlayMenuHandler(IHandler):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.PLAY.name:
                self.send(EventEnum.CREATE_AND_RUN_TURN.name)
                self.send(EventEnum.PREPARE.name)
            case EventEnum.STOP.name:
                self.send(EventEnum.STOP_TURN.name)
                self.send(EventEnum.STOP_SESSION.name)
                self.send(EventEnum.SHOW_MAIN_MENU.name)
            case EventEnum.CALLBACK_PREPARE.name:
                self._handle_callback_prepare(dto)
            case EventEnum.REPLY_PROPOSAL.name:
                self._handle_reply_proposal(dto)

    @check_dto_is_defined(EventEnum.CALLBACK_PREPARE, PrepareDTO)
    @check_dto_required_fields(EventEnum.CALLBACK_PREPARE, PrepareDTO)
    def _handle_callback_prepare(self, dto: IDto = None) -> None:
        self.send(EventEnum.ASK_PROPOSAL.name, dto)

    @check_dto_is_defined(EventEnum.REPLY_PROPOSAL, FeedbackDTO)
    @check_dto_required_fields(EventEnum.REPLY_PROPOSAL, FeedbackDTO)
    def _handle_reply_proposal(self, dto: IDto = None) -> None:
        self.send(EventEnum.SHOW_FEEDBACK.name, dto)
