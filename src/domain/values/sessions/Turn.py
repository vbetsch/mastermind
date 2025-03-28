from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class Turn:
    def __init__(self) -> None:
        self.status: StatusEnum = StatusEnum.NOT_STARTED
        self.feedback: Feedback | None = None
        self.proposal: Combination | None = None
