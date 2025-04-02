from src.common.communication.Subscriber import Subscriber
from src.common.communication.data.IData import IData
from src.common.patterns.mediator.IMediator import IMediator


class Mediator(IMediator):
    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []

    def send_message(self, message: str, sender: Subscriber, data: IData = None) -> None:
        for subscriber in self._subscribers:
            if subscriber != sender:
                subscriber.receive(message, sender, data)

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
