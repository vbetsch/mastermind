from abc import ABC, abstractmethod

from src.common.communication.Data import Data


class IMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender, data: Data | None = None) -> None:
        pass

    @abstractmethod
    def subscribe(self, subscriber) -> None:
        pass
