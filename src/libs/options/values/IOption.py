from abc import ABC


class IOption(ABC):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"IOption(name='{self.name}', value='{self.value}')"
