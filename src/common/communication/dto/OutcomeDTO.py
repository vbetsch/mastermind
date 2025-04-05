from src.common.communication.OutcomeEnum import OutcomeEnum
from src.common.communication.dto.IDto import IDto


class OutcomeDTO(IDto):
    def __init__(self, outcome: OutcomeEnum):
        self.outcome: OutcomeEnum = outcome
