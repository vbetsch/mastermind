from src.common.dto.IDto import IDto
from src.common.enums.OutcomeEnum import OutcomeEnum


class StatsDTO(IDto):
    def __init__(self, outcome: OutcomeEnum, attempts_number: int, secret_combination: str):
        self.outcome: OutcomeEnum = outcome
        self.attempts_number: int = attempts_number
        self.secret_combination: str = secret_combination
