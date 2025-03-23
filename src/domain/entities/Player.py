from dataclasses import dataclass, field

from src.domain.values.sessions.SessionHistory import SessionHistory

@dataclass(frozen=True)
class Player:
    name: str
    sessions: SessionHistory = field(default_factory=SessionHistory)
