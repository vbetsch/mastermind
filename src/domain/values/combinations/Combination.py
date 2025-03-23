from src.domain.values.combinations.Bead import Bead


class Combination:
    def __init__(self, beads: list[Bead]):
        self.beads: list[Bead] = beads

    def __repr__(self):
        return f"Combination={[bead.color.value for bead in self.beads]}"
