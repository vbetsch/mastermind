from abc import abstractmethod
from typing import Self

from src.common.dto.IDto import IDto
from src.common.patterns.mediator.IComponent import IComponent


class Subscriber(IComponent):
    def receive(self, message: str, sender: Self, dto: IDto = None) -> None:
        self.handle(message, sender, dto)

    @abstractmethod
    def handle(self, message: str, sender: Self, dto: IDto = None) -> None:
        pass
