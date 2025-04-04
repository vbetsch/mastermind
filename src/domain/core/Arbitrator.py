from src.app.exceptions.ProposalException import ProposalException
from src.domain.core.Rules import Rules


class Arbitrator:
    def __init__(self, proposal: str) -> None:
        self._proposal: str = proposal

    def has_right_length(self) -> bool:
        if len(self._proposal) != Rules().get_beads_per_combination():
            raise ProposalException(f"Proposal {self._proposal} has wrong length")
        return True

    def has_only_available_colors(self, available_colors: dict[str, str]) -> bool:
        for char in self._proposal:
            if not char.upper() in available_colors.keys():
                raise ProposalException(f"Proposal {self._proposal} has unavailable color")
        return True
