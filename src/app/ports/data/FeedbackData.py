from src.app.ports.data.IData import IData
from src.domain.values.turns.Feedback import Feedback


class FeedbackData(IData):
    def __init__(self, feedback: Feedback):
        self.feedback: Feedback = feedback
