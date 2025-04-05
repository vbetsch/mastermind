from .IDto import IDto
from ..enums.OutcomeEnum import OutcomeEnum


class OutcomeDTO(IDto):
    def __init__(self, outcome: OutcomeEnum):
        self.outcome: OutcomeEnum = outcome
