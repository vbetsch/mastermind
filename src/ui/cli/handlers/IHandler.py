from abc import abstractmethod

from src.common.communication.Subscriber import Subscriber


class IHandler(Subscriber):
    def handle(self, message: str, sender: Subscriber) -> None:
        self.manage(message)

    @abstractmethod
    def manage(self, message: str) -> str:
        pass
