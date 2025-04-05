from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.enums.OutcomeEnum import OutcomeEnum


class StatsDTO(IDto):
    def __init__(self, outcome: OutcomeEnum, attempts_number: int):
        self.outcome: OutcomeEnum = outcome
        self.attempts_number: int = attempts_number
