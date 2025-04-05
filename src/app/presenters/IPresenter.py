from abc import ABC, abstractmethod

from src.app.data.IData import IData
from src.common.dto.IDto import IDto


class IPresenter(ABC):
    def __init__(self, data: IData):
        self.data: IData = data

    @abstractmethod
    def present(self) -> IDto:
        pass
