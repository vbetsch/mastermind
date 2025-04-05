from src.app.data.IData import IData
from src.domain.values.stages.StateEnum import StateEnum


class StateData(IData):
    def __init__(self, state: StateEnum):
        self.state: StateEnum = state
