from abc import abstractmethod
from typing import Self

from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IComponent import IComponent


class Subscriber(IComponent):
    def receive(self, message: str, sender: Self, data: IDto = None) -> None:
        self.handle(message, sender, data)

    @abstractmethod
    def handle(self, message: str, sender: Self, data: IDto = None) -> None:
        pass
