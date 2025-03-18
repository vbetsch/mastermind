from src.libs.mediators.IMediator import IMediator


class Mediator(IMediator):
    def __init__(self):
        self._subscribers: list = []

    def send_message(self, message: str, sender) -> None:
        for subscriber in self._subscribers:
            if subscriber != sender:
                subscriber.receive(message, sender)

    def subscribe(self, subscriber) -> None:
        self._subscribers.append(subscriber)
