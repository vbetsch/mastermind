from .IData import IData


class MaxAttemptsData(IData):
    def __init__(self, max_attempts: int) -> None:
        self.max_attempts: int = max_attempts
