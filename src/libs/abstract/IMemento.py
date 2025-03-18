from abc import ABC, abstractmethod


class IMemento(ABC):
    @abstractmethod
    def get_saved_state(self):
        pass
