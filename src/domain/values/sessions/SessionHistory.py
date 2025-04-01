from src.common.exceptions.MementoException import MementoException
from src.common.patterns.memento.ICareTaker import ICareTaker


class SessionHistory(ICareTaker):
    def get_last_session(self):
        try:
            return self.get_last_memento().get_saved_state()
        except MementoException:
            return None
