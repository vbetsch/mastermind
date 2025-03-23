from src.common.communication.IMediator import IMediator
from src.common.communication.Subscriber import Subscriber


class Mediator(IMediator):
    def __init__(self):
        self._subscribers: list[Subscriber] = []

    def send_message(self, message: str, sender: Subscriber) -> None:
        for subscriber in self._subscribers:
            if subscriber != sender:
                subscriber.receive(message, sender)

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
