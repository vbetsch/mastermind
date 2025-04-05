from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase


class IEndSession(IUseCase):
    @abstractmethod
    def execute(self) -> None:
        pass
