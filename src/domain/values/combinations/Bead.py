from src.domain.values.combinations.BeadColorEnum import BeadColorEnum


class Bead:
    def __init__(self, color: BeadColorEnum) -> None:
        self._color: BeadColorEnum = color

    def __repr__(self) -> str:
        return f"Bead(color='{self._color.value}')"

    def get_color(self) -> str:
        return self._color.value
