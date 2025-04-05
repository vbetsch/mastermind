from src.common.communication.OutcomeEnum import OutcomeEnum
from .IDto import IDto


class OutcomeDTO(IDto):
    def __init__(self, outcome: OutcomeEnum):
        self.outcome: OutcomeEnum = outcome
