from src.app.ports.repositories.IHistoryRepository import IHistoryRepository
from src.domain.values.sessions.SessionHistory import SessionHistory


class HistoryRepository(IHistoryRepository):
    def find(self, value) -> SessionHistory | None:
        pass

    def create(self, history: SessionHistory) -> int:
        pass

    def update(self, history: SessionHistory) -> None:
        pass

    def delete(self, history: SessionHistory) -> None:
        pass
