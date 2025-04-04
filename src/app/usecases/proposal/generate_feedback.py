from src.app.ports.usecases.proposal.IGenerateFeedback import IGenerateFeedback
from src.common.logs.Logger import Logger
from src.domain.core.Arbitrator import Arbitrator
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class GenerateFeedback(IGenerateFeedback):
    def execute(self, combination: Combination) -> Feedback:
        feedback: Feedback = Arbitrator().generate_feedback(combination)
        Logger().debug(f"Generated feedback: {feedback}")
        return feedback
