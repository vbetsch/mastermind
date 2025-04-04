from src.app.ports.usecases.prepare.IGetAvailableColors import IGetAvailableColors
from src.app.ports.usecases.proposal.ICreateCombination import ICreateCombination
from src.common.logs.Logger import Logger
from src.domain.core.Arbitrator import Arbitrator
from src.domain.core.Generator import Generator
from src.domain.values.combinations.Combination import Combination


class CreateCombination(ICreateCombination):
    def __init__(self, get_available_colors: IGetAvailableColors):
        super().__init__()
        self._get_available_colors: IGetAvailableColors = get_available_colors

    @staticmethod
    def _run_proposal_checks(proposal: str, available_colors: dict[str, str]) -> None:
        arbitrator: Arbitrator = Arbitrator(proposal)
        arbitrator.has_right_length()
        arbitrator.has_only_available_colors(available_colors)

    def execute(self, proposal: str) -> Combination:
        self._run_proposal_checks(proposal, self._get_available_colors.execute())
        combination: Combination = Generator().generate_combination(proposal)
        Logger().debug(f"Create combination: {combination}")
        return combination
