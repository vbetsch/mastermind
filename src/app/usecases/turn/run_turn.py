from src.app.ports.usecases.turn.IRunTurn import IRunTurn
from src.common.logs.Logger import Logger
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.sessions.Turn import Turn


class RunTurn(IRunTurn):
    def execute(self) -> None:
        session: Session = Storage().get_current_session()
        Logger().info(f"The secret combination is {session.get_secret_combination()}")
        turn: Turn = Storage().get_current_turn()
        turn.run()
