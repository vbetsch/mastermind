from abc import ABC, abstractmethod

from src.libs.callbacks.ICallback import ICallback
from src.libs.enums.OptionEnum import OptionEnum


class IController(ABC):
    @abstractmethod
    def handle(self, choice: OptionEnum) -> ICallback | None:
        pass
