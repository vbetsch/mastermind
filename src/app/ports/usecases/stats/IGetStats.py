from src.app.data.StatsData import StatsData
from src.app.ports.usecases.IUseCase import IUseCase


class IGetStats(IUseCase):
    def execute(self) -> StatsData:
        pass
