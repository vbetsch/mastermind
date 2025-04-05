from .IData import IData
from .MaxAttemptsData import MaxAttemptsData
from .PreviousAttemptsData import PreviousAttemptsData
from ...domain.values.turns.Attempt import Attempt


class PrepareData(IData):
    def __init__(self,
                 available_colors: dict[str, str],
                 previous_attempts: PreviousAttemptsData,
                 beads_per_combination: int,
                 max_attempts: MaxAttemptsData) -> None:
        self.available_colors: dict[str, str] = available_colors
        self.previous_attempts: PreviousAttemptsData = previous_attempts
        self.beads_per_combination: int = beads_per_combination
        self.max_attempts: MaxAttemptsData = max_attempts

    def get_previous_attempts(self) -> list[Attempt]:
        return self.previous_attempts.attempts

    def get_max_attempts(self) -> int:
        return self.max_attempts.max_attempts
