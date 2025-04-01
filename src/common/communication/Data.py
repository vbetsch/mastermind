from src.domain.entities.Player import Player


class Data:
    def __init__(self, player: Player | None = None) -> None:
        self.player: Player | None = player
