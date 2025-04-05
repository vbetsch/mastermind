from abc import abstractmethod

from src.common.communication.Subscriber import Subscriber
from src.common.dto.IDto import IDto


class IHandler(Subscriber):
    @abstractmethod
    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        pass
