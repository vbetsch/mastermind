from abc import ABC, abstractmethod
from typing import Self

from src.common.abstract.mediator.IMediator import IMediator


class IComponent(ABC):
    def __init__(self, name: str, mediator: IMediator) -> None:
        self.name: str = name
        self.mediator: IMediator = mediator
        self.mediator.subscribe(self)

    def send(self, message: str) -> None:
        self.mediator.send_message(message, self)

    @abstractmethod
    def receive(self, message: str, sender: Self) -> None:
        pass
