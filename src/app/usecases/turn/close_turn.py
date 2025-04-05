from src.app.ports.usecases.turn.ICloseTurn import ICloseTurn
from src.domain.core.Storage import Storage
from src.domain.values.sessions.Turn import Turn


class CloseTurn(ICloseTurn):
    def execute(self) -> None:
        turn: Turn = Storage().get_current_turn()
        turn.close()
        Storage().set_current_turn(turn)
