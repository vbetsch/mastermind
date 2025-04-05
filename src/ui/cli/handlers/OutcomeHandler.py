from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.decorators.dto.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.dto.check_dto_required_fields import check_dto_required_fields
from src.common.dto.IDto import IDto
from src.common.dto.OutcomeDTO import OutcomeDTO
from src.common.enums.OutcomeEnum import OutcomeEnum
from src.common.logs.Logger import Logger
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class OutcomeHandler(IHandler):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.OUTCOME.name:
                self._handle_callback_state(dto)

    @check_dto_is_defined(EventEnum.OUTCOME, OutcomeDTO)
    @check_dto_required_fields(EventEnum.OUTCOME, OutcomeDTO)
    def _handle_callback_state(self, dto: OutcomeDTO = None) -> None:
        match dto.outcome:
            case OutcomeEnum.VICTORY:
                self.send(EventEnum.VICTORY.name)
            case OutcomeEnum.DEFEAT:
                self.send(EventEnum.DEFEAT.name)
            case _:
                Logger().debug(f"Try again...")
                self.send(EventEnum.SHOW_PLAY_MENU.name)
