from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.values.combinations.Combination import Combination


class IGetPreviousProposals(IUseCase):
    @abstractmethod
    def execute(self) -> list[Combination]:
        pass
