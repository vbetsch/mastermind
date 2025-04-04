from random import choice

from src.common.decorators.Singleton import Singleton
from src.domain.core.Rules import Rules
from src.domain.values.combinations.Bead import Bead
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum
from src.domain.values.combinations.Combination import Combination

@Singleton
class Generator:
    nb_beads: int = Rules().get_beads_per_combination()

    @staticmethod
    def _generate_random_bead() -> Bead:
        color_picked: BeadColorEnum = choice(list(BeadColorEnum))
        return Bead(color_picked)

    @staticmethod
    def _generate_bead(color_key: str) -> Bead:
        color: BeadColorEnum = BeadColorEnum[color_key]  # type: ignore
        return Bead(color)

    def generate_random_combination(self) -> Combination:
        beads: list[Bead] = []
        for _ in range(self.nb_beads):
            beads.append(self._generate_random_bead())
        return Combination(beads)

    def generate_combination(self, string: str):
        beads: list[Bead] = []
        for index in range(self.nb_beads):
            beads.append(self._generate_bead(string.upper()[index]))
        return Combination(beads)
