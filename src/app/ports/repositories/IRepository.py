from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def create(self, entity) -> int:
        pass

    @abstractmethod
    def update(self, entity):
        pass
