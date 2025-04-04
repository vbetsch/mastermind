from abc import abstractmethod

from src.app.ports.usecases.IUseCase import IUseCase
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class IGenerateFeedback(IUseCase):
    @abstractmethod
    def execute(self, combination: Combination) -> Feedback:
        pass
