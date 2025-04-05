from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.values.stages.StateEnum import StateEnum


class IGetState(IUseCase):
    @abstractmethod
    def execute(self) -> StateEnum:
        pass
