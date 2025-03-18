from src.domain.values.combinations.Unit import Unit


class Combination:
    def __init__(self, units: list[Unit]) -> None:
        self._units: list[Unit] = units
