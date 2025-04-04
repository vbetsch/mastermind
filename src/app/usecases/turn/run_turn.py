from src.app.ports.usecases.turn.IRunTurn import IRunTurn
from src.domain.core.Storage import Storage
from src.domain.values.sessions.Turn import Turn


class RunTurn(IRunTurn):
    def execute(self) -> None:
        turn: Turn = Storage().get_current_turn()
        turn.run()
