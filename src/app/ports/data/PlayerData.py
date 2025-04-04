from src.app.ports.data.IData import IData
from src.domain.entities.Player import Player


class PlayerData(IData):
    def __init__(self, player: Player):
        self.player = player
