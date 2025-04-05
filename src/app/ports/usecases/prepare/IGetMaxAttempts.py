from src.app.data.MaxAttemptsData import MaxAttemptsData
from ..IUseCase import IUseCase


class IGetMaxAttempts(IUseCase):
    def execute(self) -> MaxAttemptsData:
        pass
