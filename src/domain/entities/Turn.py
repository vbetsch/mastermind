from dataclasses import dataclass

from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.turn.Feedback import Feedback


@dataclass(frozen=True)
class Turn:
    status: StatusEnum
    feedback: Feedback
