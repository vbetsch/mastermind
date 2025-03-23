from abc import ABC, abstractmethod
from typing import Self

from src.common.abstract.memento.IMemento import IMemento


class IOriginator(ABC):
    @abstractmethod
    def save(self) -> IMemento:
        pass

    @abstractmethod
    def restore(self, memento: IMemento) -> Self:
        pass
