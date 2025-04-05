from src.app.controllers.IController import IController
from src.app.data.StatsData import StatsData
from src.app.ports.usecases.stats.IGetStats import IGetStats
from src.app.presenters.StatsPresenter import StatsPresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator


class StatsController(IController):
    def __init__(self, mediator: IMediator,
                 get_stats: IGetStats):
        super().__init__(self.__class__.__name__, mediator)
        self._get_stats: IGetStats = get_stats

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.VICTORY.name:
                self._handle_victory_or_defeat()
            case EventEnum.DEFEAT.name:
                self._handle_victory_or_defeat()

    def _handle_victory_or_defeat(self):
        stats: StatsData = self._get_stats.execute()
        presenter: StatsPresenter = StatsPresenter(stats)
        self.send(EventEnum.DISPLAY_STATS.name, presenter.present())
