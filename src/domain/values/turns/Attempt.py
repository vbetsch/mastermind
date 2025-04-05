from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class Attempt:
    def __init__(self, combination: Combination, feedback: Feedback) -> None:
        self._combination: Combination = combination
        self._feedback: Feedback = feedback

    def get_combination(self) -> Combination:
        return self._combination

    def get_feedback(self) -> Feedback:
        return self._feedback
