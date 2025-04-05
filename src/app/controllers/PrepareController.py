from .IController import IController
from src.app.data.PrepareData import PrepareData
from src.app.data.PreviousAttemptsData import PreviousAttemptsData
from src.app.ports.usecases.prepare.IGetAvailableColors import IGetAvailableColors
from src.app.ports.usecases.prepare.IGetBeadsPerCombination import IGetBeadsPerCombination
from src.app.ports.usecases.prepare.IGetMaxAttempts import IGetMaxAttempts
from src.app.ports.usecases.prepare.IGetPreviousAttempts import IGetPreviousAttempts
from src.app.presenters.PreparePresenter import PreparePresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator
from ..data.MaxAttemptsData import MaxAttemptsData


class PrepareController(IController):
    def __init__(self, mediator: IMediator,
                 get_available_colors: IGetAvailableColors,
                 get_previous_attempts: IGetPreviousAttempts,
                 get_beads_per_combination: IGetBeadsPerCombination,
                 get_max_attempts: IGetMaxAttempts) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._get_available_colors: IGetAvailableColors = get_available_colors
        self._get_previous_attempts: IGetPreviousAttempts = get_previous_attempts
        self._get_beads_per_combination: IGetBeadsPerCombination = get_beads_per_combination
        self._get_max_attempts: IGetMaxAttempts = get_max_attempts

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.PREPARE.name:
                available_colors: dict[str, str] = self._get_available_colors.execute()
                previous_attempts: PreviousAttemptsData = self._get_previous_attempts.execute()
                beads_per_combination: int = self._get_beads_per_combination.execute()
                max_attempts: MaxAttemptsData = self._get_max_attempts.execute()
                presenter: PreparePresenter = PreparePresenter(PrepareData(
                    available_colors=available_colors,
                    previous_attempts=previous_attempts,
                    beads_per_combination=beads_per_combination,
                    max_attempts=max_attempts,
                ))
                self.send(EventEnum.CALLBACK_PREPARE.name, presenter.present())
