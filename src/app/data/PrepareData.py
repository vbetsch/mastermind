from .IData import IData
from .PreviousAttemptsData import PreviousAttemptsData
from ...domain.values.turns.Attempt import Attempt


class PrepareData(IData):
    def __init__(self,
                 available_colors: dict[str, str],
                 previous_attempts: PreviousAttemptsData,
                 beads_per_combination: int) -> None:
        self.available_colors: dict[str, str] = available_colors
        self.previous_attempts: PreviousAttemptsData = previous_attempts
        self.beads_per_combination: int = beads_per_combination

    def get_previous_attempts(self) -> list[Attempt]:
        return self.previous_attempts.attempts
