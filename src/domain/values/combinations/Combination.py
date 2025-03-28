from src.domain.values.combinations.Bead import Bead


class Combination:
    def __init__(self, beads: list[Bead]) -> None:
        self.beads: list[Bead] = beads

    def __repr__(self) -> str:
        return f"Combination={[bead.color.value for bead in self.beads]}"
