from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_saved_state(self):
        pass
