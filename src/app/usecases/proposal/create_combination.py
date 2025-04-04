from src.app.ports.usecases.prepare.IGetAvailableColors import IGetAvailableColors
from src.app.ports.usecases.proposal.ICreateCombination import ICreateCombination
from src.domain.core.Arbitrator import Arbitrator
from src.domain.core.Generator import Generator
from src.domain.values.combinations.Combination import Combination


class CreateCombination(ICreateCombination):
    def __init__(self, get_available_colors: IGetAvailableColors):
        super().__init__()
        self._get_available_colors: IGetAvailableColors = get_available_colors

    @staticmethod
    def _run_proposal_checks(proposal: str, available_colors: dict[str, str]) -> None:
        Arbitrator().has_right_length(proposal)
        Arbitrator().has_only_available_colors(proposal, available_colors)

    def execute(self, proposal: str) -> Combination:
        self._run_proposal_checks(proposal, self._get_available_colors.execute())
        combination: Combination = Generator().generate_combination(proposal)
        return combination
