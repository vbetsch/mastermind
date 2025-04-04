from src.app.ports.data.IData import IData
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


class UpdateTurnData(IData):
    def __init__(self, feedback: Feedback, proposal: Combination) -> None:
        self.feedback: Feedback = feedback
        self.proposal: Combination = proposal
