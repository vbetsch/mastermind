from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase


class IGetBeadsPerCombination(IUseCase):
    @abstractmethod
    def execute(self) -> int:
        pass
