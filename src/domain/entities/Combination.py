from dataclasses import dataclass, field

from src.domain.values.combinations.Unit import Unit

@dataclass(frozen=True)
class Combination:
    units: list[Unit] = field(default_factory=list[Unit])
