from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.values.sessions.SessionHistory import SessionHistory


class IHistoryRepository(IRepository):
    @abstractmethod
    def find(self, history_id: int) -> SessionHistory | None:
        pass

    @abstractmethod
    def create(self, history: SessionHistory, dependency=None) -> int:
        pass

    @abstractmethod
    def update(self, history: SessionHistory) -> None:
        pass

    @abstractmethod
    def delete(self, history: SessionHistory) -> None:
        pass
