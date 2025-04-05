from src.common.logs.Logger import Logger
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class Turn:
    def __init__(self) -> None:
        self._status: StatusEnum = StatusEnum.NOT_STARTED
        self._feedback: Feedback | None = None
        self._proposal: Combination | None = None

    def get_if_proposal(self) -> Combination | None:
        return self._proposal

    def set_feedback(self, feedback: Feedback) -> None:
        self._feedback = feedback

    def set_proposal(self, proposal: Combination) -> None:
        self._proposal = proposal

    def run(self) -> None:
        self._status = StatusEnum.RUNNING
        Logger().log("Turn started")

    def stop(self) -> None:
        self._status = StatusEnum.STOPPED
        Logger().log("Turn stopped", line_break=True)

    def close(self) -> None:
        self._status = StatusEnum.DONE
        Logger().log("Turn closed")
