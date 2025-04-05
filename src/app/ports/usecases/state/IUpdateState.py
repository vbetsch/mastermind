from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase


class IUpdateState(IUseCase):
    @abstractmethod
    def execute(self) -> None:
        pass
