from abc import abstractmethod
from typing import Self

from src.common.patterns.mediator.IComponent import IComponent


class Subscriber(IComponent):
    def receive(self, message: str, sender: Self) -> None:
        self.handle(message, sender)

    @abstractmethod
    def handle(self, message: str, sender: Self) -> None:
        pass
