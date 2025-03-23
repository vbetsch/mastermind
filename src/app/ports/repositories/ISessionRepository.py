from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.entities.Session import Session


class ISessionRepository(IRepository):
    @abstractmethod
    def create(self, session: Session):
        pass
