from src.common.communication.dto.IDto import IDto


class PrepareDTO(IDto):
    def __init__(self, available_colors: dict[str, str], previous_proposals: list[str], beads_per_combination: int):
        self.available_colors: dict[str, str] = available_colors
        self.previous_proposals: list[str] = previous_proposals
        self.beads_per_combination: int = beads_per_combination
