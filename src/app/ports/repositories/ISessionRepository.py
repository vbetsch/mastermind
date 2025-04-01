from abc import abstractmethod

from src.app.ports.repositories.IRepository import IRepository
from src.domain.entities.Session import Session


class ISessionRepository(IRepository):
    @abstractmethod
    def find(self, value) -> Session | None:
        pass

    @abstractmethod
    def create(self, session: Session, dependency=None) -> int:
        pass

    @abstractmethod
    def update(self, session: Session) -> None:
        pass

    @abstractmethod
    def delete(self, session: Session) -> None:
        pass
