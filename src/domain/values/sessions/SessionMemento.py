from src.common.abstract.memento.IMemento import IMemento


class SessionMemento(IMemento):
    def __init__(self, state) -> None:
        self._state = state

    def get_saved_state(self):
        return self._state
