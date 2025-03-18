from abc import ABC, abstractmethod


class IUseCase(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass
