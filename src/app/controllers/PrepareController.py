from typing import Dict

from src.app.controllers.IController import IController
from src.app.ports.usecases.prepare.IGetAllColors import IGetAllColors
from src.app.ports.usecases.prepare.IGetPreviousProposals import IGetPreviousProposals
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.patterns.mediator.IMediator import IMediator


class PrepareController(IController):
    def __init__(self, mediator: IMediator,
                 get_all_colors: IGetAllColors,
                 get_previous_proposals: IGetPreviousProposals) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._get_all_colors: IGetAllColors = get_all_colors
        self._get_previous_proposals: IGetPreviousProposals = get_previous_proposals

    def handle(self, message: str, sender: Subscriber, data: IDto = None) -> None:
        match message:
            case EventEnum.PREPARE.name:
                all_colors: Dict[str, str] = self._get_all_colors.execute()
                previous_proposals: list[str] = self._get_previous_proposals.execute()
                self.send(EventEnum.CALLBACK_PREPARE.name, PrepareDTO(all_colors, previous_proposals))
