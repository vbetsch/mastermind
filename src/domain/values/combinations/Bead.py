from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class Bead:
    def __init__(self, color: BeadColorEnum) -> None:
        self.color: BeadColorEnum = color

    def __repr__(self) -> str:
        return f"Bead(color='{self.color.value}')"
