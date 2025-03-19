from random import choice

from src.common.decorators.Singleton import Singleton
from src.domain.entities.Combination import Combination
from src.domain.values.combinations.Unit import Unit
from src.domain.values.combinations.UnitColorEnum import UnitColorEnum


@Singleton
class Generator:
    nb_units: int = 4

    def generate_unit(self) -> Unit:
        color_picked: UnitColorEnum = choice(list(UnitColorEnum))
        return Unit(color_picked)

    def generate_combination(self) -> Combination:
        units: list[Unit] = []
        for _ in range(self.nb_units):
            units.append(self.generate_unit())
        return Combination(units)
