from abc import ABC


class IEvent(ABC):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Event(name='{self.name}', value='{self.value}')"
