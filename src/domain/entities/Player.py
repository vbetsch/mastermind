from dataclasses import dataclass, field

from src.domain.values.players.StateEnum import StateEnum
from src.domain.values.sessions.SessionHistory import SessionHistory


@dataclass(frozen=False)
class Player:
    name: str
    id: int | None = None
    state: StateEnum = StateEnum.INSIDE_MENUS
    sessions: SessionHistory = field(default_factory=SessionHistory)
    history_id: int | None = None

    def set_state(self, state: StateEnum) -> None:
        self.state = state
