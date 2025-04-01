from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.domain.entities.Player import Player


class GetOrCreatePlayer(IPlayerUseCase):
    def __init__(self, player_repository: IPlayerRepository) -> None:
        self.player_repository: IPlayerRepository = player_repository

    def execute(self, arg=None) -> Player:
        player_name: str = "default"
        player: Player | None = self.player_repository.find(name=player_name)

        if player:
            print(f"User found: {player}")
            return player

        print("Creating new user...")
        new_player: Player = Player(name=player_name)
        player_id: int = self.player_repository.create(new_player)
        new_player.id = player_id
        print(f"New user created! {new_player}")

        return new_player
