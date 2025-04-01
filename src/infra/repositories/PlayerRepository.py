from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.domain.entities.Player import Player
from src.infra.database.DatabaseConfig import DatabaseConfig
from src.infra.database.models.PlayerModel import PlayerModel


class PlayerRepository(IPlayerRepository):
    def find(self, name: str) -> Player | None:
        DatabaseConfig().connect()
        result: PlayerModel | None = PlayerModel.get_or_none(PlayerModel.name == name)
        DatabaseConfig().close()
        if not result:
            return None
        return Player(
            name=result.name,
            state=result.state,
        )

    def create(self, player: Player) -> int:
        DatabaseConfig().connect()
        player_model: PlayerModel = PlayerModel.create(
            name = player.name,
            state = player.state
        )
        DatabaseConfig().close()
        return player_model.get_id()

    def update(self, player: Player) -> None:
        pass

    def delete(self, player: Player) -> None:
        pass
