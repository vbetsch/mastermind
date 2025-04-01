from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def create(self, entity) -> int:
        pass

    @abstractmethod
    def update(self, entity) -> None:
        pass

    @abstractmethod
    def delete(self, entity) -> None:
        pass
