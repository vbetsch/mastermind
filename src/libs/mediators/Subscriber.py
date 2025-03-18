from typing import Self

from src.libs.mediators.IMediator import IMediator


class Subscriber:
    def __init__(self, name: str, mediator: IMediator) -> None:
        self.name: str = name
        self.mediator: IMediator = mediator
        self.mediator.subscribe(self)

    def send(self, message: str) -> None:
        self.mediator.send_message(message, self)

    def receive(self, message: str, sender: Self) -> None:
        self.handle(message, sender)

    def handle(self, message: str, sender: Self) -> None:
        pass
