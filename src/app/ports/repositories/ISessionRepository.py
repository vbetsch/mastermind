from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.entities.Session import Session


class ISessionRepository(IRepository):
    @abstractmethod
    def create(self, session: Session) -> int:
        pass

    @abstractmethod
    def update(self, session: Session):
        pass
