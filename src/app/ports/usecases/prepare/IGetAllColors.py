from abc import abstractmethod
from typing import Dict

from src.app.ports.usecases.IUseCase import IUseCase


class IGetAllColors(IUseCase):
    @abstractmethod
    def execute(self) -> Dict[str, str]:
        pass
