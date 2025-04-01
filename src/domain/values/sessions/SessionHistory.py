from src.common.exceptions.MementoException import MementoException
from src.common.patterns.memento.ICareTaker import ICareTaker


class SessionHistory(ICareTaker):
    def __init__(self):
        super().__init__()
        self._id: int | None = None

    def get_last_session(self):
        try:
            return self.get_last_memento().get_saved_state()
        except MementoException:
            return None

    def get_id(self) -> int:
        return self._id

    def set_id(self, value: int):
        self._id = value
