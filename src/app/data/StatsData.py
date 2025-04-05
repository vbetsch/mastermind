from src.app.data.IData import IData
from src.domain.values.combinations.Combination import Combination
from src.domain.values.stages.StateEnum import StateEnum


class StatsData(IData):
    def __init__(self, state: StateEnum, attempts_number: int, secret_combination: Combination) -> None:
        self.state: StateEnum = state
        self.attempts_number: int = attempts_number
        self.secret_combination: Combination = secret_combination
