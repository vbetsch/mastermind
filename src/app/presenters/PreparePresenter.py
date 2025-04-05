from .FeedbackPresenter import FeedbackPresenter
from .IPresenter import IPresenter
from ..data.FeedbackData import FeedbackData
from ..data.PrepareData import PrepareData
from ...common.dto.FeedbackDTO import FeedbackDTO
from ...common.dto.PrepareDTO import PrepareDTO
from ...common.dto.ProposalDTO import ProposalDTO
from ...domain.values.turns.Attempt import Attempt


class PreparePresenter(IPresenter):
    def __init__(self, data: PrepareData):
        super().__init__(data)
        self.data: PrepareData = data

    @staticmethod
    def _present_proposal(attempt: Attempt) -> ProposalDTO:
        proposal: str = str(attempt.get_combination())
        return ProposalDTO(proposal)

    @staticmethod
    def _present_feedback(attempt: Attempt) -> FeedbackDTO:
        feedback_presenter: FeedbackPresenter = FeedbackPresenter(
            FeedbackData(attempt.get_feedback())
        )
        return feedback_presenter.present()

    def _present_previous_attempts(self) -> list[tuple[ProposalDTO, FeedbackDTO]]:
        result: list[tuple[ProposalDTO, FeedbackDTO]] = []
        for attempt in self.data.get_previous_attempts():
            present_attempt = (
                self._present_proposal(attempt),
                self._present_feedback(attempt)
            )
            result.append(present_attempt)
        return result

    def present(self) -> PrepareDTO:
        return PrepareDTO(
            available_colors=self.data.available_colors,
            previous_attempts=self._present_previous_attempts(),
            beads_per_combination=self.data.beads_per_combination,
        )
