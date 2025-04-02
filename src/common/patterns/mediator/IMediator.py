from abc import ABC, abstractmethod

from src.common.communication.data.IData import IData


class IMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender, data: IData = None) -> None:
        pass

    @abstractmethod
    def subscribe(self, subscriber) -> None:
        pass
