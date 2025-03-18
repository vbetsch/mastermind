from src.domain.values.StatusEnum import StatusEnum


class Turn:
    def __init__(self, status: StatusEnum) -> None:
        self._status: StatusEnum = status
