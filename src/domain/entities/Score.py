from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Score:
    value: int = 0
