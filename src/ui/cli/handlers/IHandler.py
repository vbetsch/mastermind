from abc import abstractmethod

from src.common.communication.Subscriber import Subscriber


class IHandler(Subscriber):
    @abstractmethod
    def handle(self, message: str, sender: Subscriber) -> None:
        pass
