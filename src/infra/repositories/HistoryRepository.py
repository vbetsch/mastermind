from src.app.ports.repositories.IHistoryRepository import IHistoryRepository
from src.domain.values.sessions.SessionHistory import SessionHistory
from src.infra.database.DatabaseConfig import DatabaseConfig
from src.infra.database.models.HistoryModel import HistoryModel


class HistoryRepository(IHistoryRepository):
    def find(self, history_id: int) -> SessionHistory | None:
        result: HistoryModel = HistoryModel.get(HistoryModel.id == history_id)
        DatabaseConfig().close()
        history = SessionHistory()
        history.set_id(result.id)
        return history

    def create(self, history: SessionHistory, dependency=None) -> int:
        DatabaseConfig().connect()
        history_model: HistoryModel = HistoryModel.create()
        DatabaseConfig().close()
        return history_model.get_id()

    def update(self, history: SessionHistory) -> None:
        pass

    def delete(self, history: SessionHistory) -> None:
        pass
