from src.domain.values.combinations.Bead import Bead


class Combination:
    def __init__(self, beads: list[Bead]) -> None:
        self._beads: list[Bead] = beads

    def __repr__(self) -> str:
        return f"Combination={[bead.get_color() for bead in self._beads]}"
