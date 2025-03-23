from dataclasses import dataclass, field

from src.domain.values.combinations.Bead import Bead

@dataclass(frozen=True)
class Combination:
    beads: list[Bead] = field(default_factory=list[Bead])

    def __repr__(self):
        return f"Combination={[bead.color.value for bead in self.beads]}"
