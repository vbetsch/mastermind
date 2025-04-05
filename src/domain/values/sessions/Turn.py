from src.app.exceptions.FeedbackException import FeedbackException
from src.app.exceptions.ProposalException import ProposalException
from src.common.logs.Logger import Logger
from src.domain.values.combinations.Combination import Combination
from src.domain.values.stages.StatusEnum import StatusEnum
from src.domain.values.turns.Attempt import Attempt
from src.domain.values.turns.Feedback import Feedback


class Turn:
    def __init__(self) -> None:
        self._status: StatusEnum = StatusEnum.NOT_STARTED
        self._attempt: Attempt | None = None

    def get_if_attempt(self) -> Attempt | None:
        return self._attempt

    def get_proposal(self) -> Combination:
        if not self._attempt:
            raise ProposalException("Proposal not found")
        return self._attempt.get_combination()

    def get_feedback(self) -> Feedback:
        if not self._attempt:
            raise FeedbackException("Feedback not found")
        return self._attempt.get_feedback()

    def set_attempt(self, attempt: Attempt) -> None:
        self._attempt = attempt

    def run(self) -> None:
        self._status = StatusEnum.RUNNING
        Logger().log("Turn started")

    def stop(self) -> None:
        self._status = StatusEnum.STOPPED
        Logger().log("Turn stopped", line_break=True)

    def close(self) -> None:
        self._status = StatusEnum.DONE
        Logger().log("Turn closed")
