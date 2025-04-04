from abc import ABC, abstractmethod

from src.app.ports.data.IData import IData
from src.common.communication.dto.IDto import IDto


class IPresenter(ABC):
    def __init__(self, data: IData):
        self.data: IData = data

    @abstractmethod
    def present(self) -> IDto:
        pass
