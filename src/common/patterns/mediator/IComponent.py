from abc import ABC, abstractmethod
from typing import Self

from src.common.communication.Data import Data
from src.common.patterns.mediator.IMediator import IMediator


class IComponent(ABC):
    def __init__(self, name: str, mediator: IMediator) -> None:
        self._name: str = name
        self._mediator: IMediator = mediator
        self._mediator.subscribe(self)

    def send(self, message: str, data: Data = None) -> None:
        self._mediator.send_message(message, self, data)

    @abstractmethod
    def receive(self, message: str, sender: Self, data: Data = None) -> None:
        pass
