from src.app.data.IData import IData
from src.domain.values.stages.StateEnum import StateEnum


class StatsData(IData):
    def __init__(self, state: StateEnum, attempts_number: int) -> None:
        self.state: StateEnum = state
        self.attempts_number: int = attempts_number
