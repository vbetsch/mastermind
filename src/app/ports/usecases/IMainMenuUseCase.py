from abc import abstractmethod

from src.common.abstract.IUseCase import IUseCase


class IMainMenuUseCase(IUseCase):
    @abstractmethod
    def execute(self) -> None:
        pass
