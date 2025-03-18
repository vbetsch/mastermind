from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def create(self, session):
        pass
