from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.domain.entities.Session import Session
from src.infra.database.DatabaseConfig import DatabaseConfig
from src.infra.database.models.SessionModel import SessionModel


class SessionRepository(ISessionRepository):
    def create(self, session: Session):
        DatabaseConfig().connect()
        SessionModel.create(status=session.status.value, score=session.score.value)
        DatabaseConfig().close()
        print("Session created!")
