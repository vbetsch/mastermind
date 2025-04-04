from src.common.communication.dto.IDto import IDto


class FeedbackDTO(IDto):
    def __init__(self, feedback: dict[str, int]):
        self.feedback: dict[str, int] = feedback
