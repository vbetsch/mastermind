from dataclasses import dataclass

from src.domain.values.StatusEnum import StatusEnum


@dataclass(frozen=True)
class Turn:
    status: StatusEnum
