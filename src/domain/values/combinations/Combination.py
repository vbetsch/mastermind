from src.domain.values.combinations.Bead import Bead


class Combination:
    def __init__(self, beads: list[Bead]) -> None:
        self._beads: list[Bead] = beads

    def get_beads(self) -> list[Bead]:
        return self._beads

    def get_bead_color_key(self, index: int) -> str:
        return self.get_beads()[index].get_color_key()

    def get_list_bead_color_keys(self) -> list[str]:
        return [bead.get_color_key() for bead in self._beads]

    def __repr__(self) -> str:
        return ''.join([bead.get_color_key() for bead in self._beads])
