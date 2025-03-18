from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.domain.entities.Session import Session


class SessionRepository(ISessionRepository):
    def create(self, session: Session):
        print(f"Creating the session {session}...")
