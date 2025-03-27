from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.domain.entities.Session import Session
from src.infra.database.DatabaseConfig import DatabaseConfig
from src.infra.database.models.SessionModel import SessionModel


class SessionRepository(ISessionRepository):
    def create(self, session: Session) -> int:
        DatabaseConfig().connect()
        session_model: SessionModel = SessionModel.create(
            status=session.status.name
        )
        DatabaseConfig().close()
        return session_model.get_id()

    def update(self, session: Session):
        DatabaseConfig().connect()
        session_model: SessionModel = SessionModel.get_by_id(session.id)
        session_model.status = session.status.name
        SessionModel.save(session_model)
        DatabaseConfig().close()
