from src.app.ports.usecases.turn.ICreateTurn import ICreateTurn
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.sessions.Turn import Turn


class CreateTurn(ICreateTurn):
    def execute(self) -> None:
        turn: Turn = Turn()
        Storage().set_current_turn(turn)
        session: Session = Storage().get_current_session()
        session.add_turn(turn)
        Storage().set_current_session(session)
