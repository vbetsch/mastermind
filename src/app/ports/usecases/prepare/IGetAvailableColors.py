from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase


class IGetAvailableColors(IUseCase):
    @abstractmethod
    def execute(self) -> dict[str, str]:
        pass
