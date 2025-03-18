from abc import ABC


class IMessage(ABC):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Message(name='{self.name}', value='{self.value}')"
