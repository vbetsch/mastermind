from src.common.communication.dto.IDto import IDto


class FeedbackDTO(IDto):
    def __init__(self, feedback: dict[str, str]):
        self.feedback: dict[str, str] = feedback
