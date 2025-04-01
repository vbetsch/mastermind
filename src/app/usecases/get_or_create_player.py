from src.app.ports.repositories.IHistoryRepository import IHistoryRepository
from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.domain.entities.Player import Player
from src.domain.values.sessions.SessionHistory import SessionHistory


class GetOrCreatePlayer(IPlayerUseCase):
    def __init__(self, history_repository: IHistoryRepository, player_repository: IPlayerRepository) -> None:
        self.history_repository: IHistoryRepository = history_repository
        self.player_repository: IPlayerRepository = player_repository

    def execute(self, arg=None) -> Player:
        player_name: str = "default"
        player: Player | None = self.player_repository.find(name=player_name)

        if player:
            history: SessionHistory = self.history_repository.find(history_id=player.history_id)
            player.sessions = history
            return player

        print("Creating new user...")
        new_player: Player = Player(name=player_name)
        history_id: int = self.history_repository.create(new_player.sessions)
        new_player.sessions.set_id(history_id)
        player_id: int = self.player_repository.create(new_player, history_id)
        new_player.id = player_id
        print(f"New user created!")

        return new_player
