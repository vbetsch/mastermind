from .FeedbackDTO import FeedbackDTO
from .IDto import IDto
from .ProposalDTO import ProposalDTO


class PrepareDTO(IDto):
    def __init__(self, available_colors: dict[str, str], previous_attempts: list[tuple[ProposalDTO, FeedbackDTO]], beads_per_combination: int):
        self.available_colors: dict[str, str] = available_colors
        self.previous_attempts: list[tuple[ProposalDTO, FeedbackDTO]] = previous_attempts
        self.beads_per_combination: int = beads_per_combination
