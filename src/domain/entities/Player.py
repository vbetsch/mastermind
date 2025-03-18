from src.domain.values.sessions.SessionHistory import SessionHistory


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._sessions = SessionHistory()
