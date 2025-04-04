from src.domain.values.turns.indicators.IndicatorColorEnum import IndicatorColorEnum


class Indicator:
    def __init__(self, color: IndicatorColorEnum) -> None:
        self._color: IndicatorColorEnum = color
        self._value: int = 0

    def get_color_value(self) -> str:
        return self._color.value

    def get_value(self) -> int:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = value
