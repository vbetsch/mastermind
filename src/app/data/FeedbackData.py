from src.app.data.IData import IData
from src.domain.values.turns.Feedback import Feedback
from src.domain.values.turns.indicators.Indicator import Indicator


class FeedbackData(IData):
    def __init__(self, feedback: Feedback):
        self.feedback: Feedback = feedback

    def get_indicators(self) -> list[Indicator]:
        return self.feedback.get_indicators()
