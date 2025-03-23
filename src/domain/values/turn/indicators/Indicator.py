from src.domain.values.turn.indicators.IndicatorColorEnum import IndicatorColorEnum


class Indicator:
    def __init__(self, color: IndicatorColorEnum):
        self._color: IndicatorColorEnum = color
