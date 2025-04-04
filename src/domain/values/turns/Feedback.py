from src.domain.values.turns.indicators.Indicator import Indicator
from src.domain.values.turns.indicators.IndicatorColorEnum import IndicatorColorEnum


class Feedback:
    def __init__(self) -> None:
        self._red_indicator: Indicator = Indicator(IndicatorColorEnum.RED)
        self._white_indicator: Indicator = Indicator(IndicatorColorEnum.WHITE)
        self._indicators: list[Indicator] = [self._red_indicator, self._white_indicator]

    def get_indicators(self) -> list[Indicator]:
        return self._indicators

    def get_red_indicator(self) -> Indicator:
        return self._red_indicator

    def get_white_indicator(self) -> Indicator:
        return self._white_indicator

    def set_red_indicator_value(self, value: int) -> None:
        self._red_indicator.set_value(value)

    def set_white_indicator_value(self, value: int) -> None:
        self._white_indicator.set_value(value)

    def __repr__(self) -> str:
        return ",".join([f"{indicator.get_color_value()}={indicator.get_value()}" for indicator in self._indicators])
