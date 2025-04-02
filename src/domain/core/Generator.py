from random import choice

from src.domain.core.Game import Game
from src.domain.values.combinations.Bead import Bead
from src.domain.values.combinations.BeadColorEnum import BeadColorEnum
from src.domain.values.combinations.Combination import Combination


class Generator:
    nb_beads: int = Game().get_beads_per_combination()

    @staticmethod
    def generate_bead() -> Bead:
        color_picked: BeadColorEnum = choice(list(BeadColorEnum))
        return Bead(color_picked)

    def generate_combination(self) -> Combination:
        beads: list[Bead] = []
        for _ in range(self.nb_beads):
            beads.append(self.generate_bead())
        return Combination(beads)
