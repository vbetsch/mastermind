from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase


class IGetPreviousProposals(IUseCase):
    @abstractmethod
    def execute(self) -> list[str]:
        pass
