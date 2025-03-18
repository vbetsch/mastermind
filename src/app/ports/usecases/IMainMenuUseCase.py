from abc import abstractmethod, ABC

from src.common.abstract.IUseCase import IUseCase


class IMainMenuUseCase(IUseCase):
    @abstractmethod
    def execute(self) -> None:
        pass
