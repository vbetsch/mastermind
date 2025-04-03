from abc import ABC, abstractmethod

from src.common.communication.dto.IDto import IDto


class IMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender, dto: IDto = None) -> None:
        pass

    @abstractmethod
    def subscribe(self, subscriber) -> None:
        pass
