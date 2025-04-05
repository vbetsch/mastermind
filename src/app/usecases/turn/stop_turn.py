from src.app.ports.usecases.turn.IStopTurn import IStopTurn
from src.domain.core.Storage import Storage
from src.domain.values.sessions.Turn import Turn


class StopTurn(IStopTurn):
    def execute(self) -> None:
        turn: Turn = Storage().get_current_turn()
        turn.stop()
        Storage().set_current_turn(turn)
