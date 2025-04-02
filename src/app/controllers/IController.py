from abc import abstractmethod

from src.common.communication.Subscriber import Subscriber
from src.common.communication.data.IData import IData


class IController(Subscriber):
    @abstractmethod
    def handle(self, message: str, sender: Subscriber, data: IData = None) -> None:
        pass
