from abc import ABC


class ICallback(ABC):
    def __init__(self, name: str, param=None) -> None:
        self.name: str = name
        self.param = param
