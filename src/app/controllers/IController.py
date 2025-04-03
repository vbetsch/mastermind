from abc import abstractmethod

from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto


class IController(Subscriber):
    @abstractmethod
    def handle(self, message: str, sender: Subscriber, data: IDto = None) -> None:
        pass
