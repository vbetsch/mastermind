from src.domain.values.combinations.UnitColorEnum import UnitColorEnum


class Unit:
    def __init__(self, color: UnitColorEnum) -> None:
        self.color: UnitColorEnum = color
