from src.app.data.FeedbackData import FeedbackData
from src.app.presenters.IPresenter import IPresenter
from src.common.dto.FeedbackDTO import FeedbackDTO


class FeedbackPresenter(IPresenter):
    def __init__(self, data: FeedbackData):
        super().__init__(data)
        self.data: FeedbackData = data

    def present(self) -> FeedbackDTO:
        feedback: dict[str, int] = {
            indicator.get_color_value(): indicator.get_value() for indicator in self.data.get_indicators()
        }
        return FeedbackDTO(feedback)
