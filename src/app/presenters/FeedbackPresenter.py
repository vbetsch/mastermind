from src.app.ports.data.FeedbackData import FeedbackData
from src.app.presenters.IPresenter import IPresenter
from src.common.communication.dto.FeedbackDTO import FeedbackDTO


class FeedbackPresenter(IPresenter):
    def __init__(self, data: FeedbackData):
        super().__init__(data)

    def present(self) -> FeedbackDTO:
        pass
