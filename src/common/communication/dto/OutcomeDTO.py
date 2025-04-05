from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.enums.OutcomeEnum import OutcomeEnum


class OutcomeDTO(IDto):
    def __init__(self, outcome: OutcomeEnum):
        self.outcome: OutcomeEnum = outcome
