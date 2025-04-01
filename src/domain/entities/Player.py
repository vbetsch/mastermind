from dataclasses import dataclass, field

from src.domain.values.players.StateEnum import StateEnum
from src.domain.values.sessions.SessionHistory import SessionHistory


@dataclass(frozen=True)
class Player:
    name: str
    state: StateEnum = StateEnum.INSIDE_MENUS
    sessions: SessionHistory = field(default_factory=SessionHistory)
