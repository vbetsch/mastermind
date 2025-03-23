from dataclasses import dataclass, field

from src.domain.values.combinations.Unit import Unit

@dataclass(frozen=True)
class Combination:
    units: list[Unit] = field(default_factory=list[Unit])

    def __repr__(self):
        return f"Combination={[unit.color.value for unit in self.units]}"
