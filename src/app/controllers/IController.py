from abc import abstractmethod

from src.common.communication.Data import Data
from src.common.communication.Subscriber import Subscriber


class IController(Subscriber):
    @abstractmethod
    def handle(self, message: str, sender: Subscriber, data: Data | None = None) -> None:
        pass
