from abc import ABC

from src.common.patterns.memento.IMemento import IMemento
from src.common.patterns.memento.IOriginator import IOriginator


class ICareTaker(ABC):
    def __init__(self) -> None:
        self._mementos: list[IMemento] = []

    def get_last_memento(self) -> IMemento:
        if len(self._mementos) < 1:
            raise Exception("No memento available")
        return self._mementos[-1]

    def save(self, originator: IOriginator) -> None:
        memento = originator.save()
        self._mementos.append(memento)

    def undo(self, originator: IOriginator) -> None:
        if len(self._mementos) <= 1:
            raise Exception("No memento to restore")

        self._mementos.pop()
        last_memento: IMemento = self.get_last_memento()
        originator.restore(last_memento)
