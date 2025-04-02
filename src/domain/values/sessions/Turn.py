from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class Turn:
    def __init__(self) -> None:
        self._status: StatusEnum = StatusEnum.NOT_STARTED
        self._feedback: Feedback | None = None
        self._proposal: Combination | None = None
