from dataclasses import dataclass

from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


@dataclass(frozen=True)
class Turn:
    status: StatusEnum
    feedback: Feedback
    proposal: Combination | None = None
