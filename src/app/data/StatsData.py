from src.app.data.IData import IData


class StatsData(IData):
    def __init__(self, attempts_number: int) -> None:
        self.attempts_number: int = attempts_number
