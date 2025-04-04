from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.values.combinations.Combination import Combination


class ICreateCombination(IUseCase):
    @abstractmethod
    def execute(self, proposal: str) -> Combination:
        pass
