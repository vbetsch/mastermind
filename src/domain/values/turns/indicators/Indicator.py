from src.domain.values.turns.indicators.IndicatorColorEnum import IndicatorColorEnum


class Indicator:
    def __init__(self, color: IndicatorColorEnum):
        self._color: IndicatorColorEnum = color
