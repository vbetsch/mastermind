from src.domain.values.turns.indicators.Indicator import Indicator
from src.domain.values.turns.indicators.IndicatorColorEnum import IndicatorColorEnum


class Feedback:
    def __init__(self):
        self._red_indicator = Indicator(IndicatorColorEnum.RED)
        self._white_indicator = Indicator(IndicatorColorEnum.WHITE)
        self.indicators: list[Indicator] = [self._red_indicator, self._white_indicator]
