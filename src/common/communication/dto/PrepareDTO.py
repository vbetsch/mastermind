from typing import Dict

from src.common.communication.dto.IDto import IDto


class PrepareDTO(IDto):
    def __init__(self, all_colors: Dict[str, str], previous_proposals: list[str]):
        self.all_colors: Dict[str, str] = all_colors
        self.previous_proposals: list[str] = previous_proposals
