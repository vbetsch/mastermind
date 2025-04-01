from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.values.sessions.SessionHistory import SessionHistory


class IHistoryRepository(IRepository):
    @abstractmethod
    def create(self, history: SessionHistory) -> int:
        pass

    @abstractmethod
    def update(self, history: SessionHistory) -> None:
        pass
