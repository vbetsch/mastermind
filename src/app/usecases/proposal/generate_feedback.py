from src.app.ports.usecases.proposal.IGenerateFeedback import IGenerateFeedback
from src.domain.core.Arbitrator import Arbitrator
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class GenerateFeedback(IGenerateFeedback):
    def execute(self, combination: Combination) -> Feedback:
        return Arbitrator().generate_feedback(combination)
