from .IData import IData
from ...domain.values.turns.Attempt import Attempt


class PreviousAttemptsData(IData):
    def __init__(self, attempts: list[Attempt]):
        self.attempts: list[Attempt] = attempts
