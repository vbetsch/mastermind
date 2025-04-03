from src.app.presenters.IPresenter import IPresenter
from src.domain.entities.Player import Player


class PlayerPresenter(IPresenter):
    def __init__(self, player: Player):
        self.player = player
