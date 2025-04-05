from abc import abstractmethod

from src.app.data.PreviousAttemptsData import PreviousAttemptsData
from src.app.ports.usecases.IUseCase import IUseCase


class IGetPreviousAttempts(IUseCase):
    @abstractmethod
    def execute(self) -> PreviousAttemptsData:
        pass
