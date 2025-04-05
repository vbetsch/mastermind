from src.app.controllers.IController import IController
from src.app.ports.usecases.prepare.IGetAvailableColors import IGetAvailableColors
from src.app.ports.usecases.prepare.IGetBeadsPerCombination import IGetBeadsPerCombination
from src.app.ports.usecases.prepare.IGetPreviousProposals import IGetPreviousProposals
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.dto.IDto import IDto
from src.common.dto.PrepareDTO import PrepareDTO
from src.common.patterns.mediator.IMediator import IMediator


class PrepareController(IController):
    def __init__(self, mediator: IMediator,
                 get_available_colors: IGetAvailableColors,
                 get_previous_proposals: IGetPreviousProposals,
                 get_beads_per_combination: IGetBeadsPerCombination) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._get_available_colors: IGetAvailableColors = get_available_colors
        self._get_previous_proposals: IGetPreviousProposals = get_previous_proposals
        self._get_beads_per_combination: IGetBeadsPerCombination = get_beads_per_combination

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.PREPARE.name:
                available_colors: dict[str, str] = self._get_available_colors.execute()
                previous_proposals: list[str] = self._get_previous_proposals.execute()
                beads_per_combination: int = self._get_beads_per_combination.execute()
                self.send(
                    EventEnum.CALLBACK_PREPARE.name,
                    PrepareDTO(
                        available_colors=available_colors,
                        previous_proposals=previous_proposals,
                        beads_per_combination=beads_per_combination
                    )
                )
