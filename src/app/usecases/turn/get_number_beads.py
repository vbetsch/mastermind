from src.app.ports.usecases.turn.IGetBeadsPerCombination import IGetBeadsPerCombination
from src.domain.core.Rules import Rules


class GetBeadsPerCombination(IGetBeadsPerCombination):
    def execute(self) -> int:
        return Rules().get_beads_per_combination()
