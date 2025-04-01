from abc import ABC, abstractmethod

class IMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender, data=None) -> None:
        pass

    @abstractmethod
    def subscribe(self, subscriber) -> None:
        pass
