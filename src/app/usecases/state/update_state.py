from src.app.ports.usecases.state.IUpdateState import IUpdateState
from src.domain.core.Arbitrator import Arbitrator
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.sessions.Turn import Turn
from src.domain.values.stages.StateEnum import StateEnum


class UpdateState(IUpdateState):
    def execute(self) -> None:
        state: StateEnum = Storage().get_state()

        if state != StateEnum.PLAYING:
            Storage().set_state(StateEnum.PLAYING)
            return

        session: Session = Storage().get_current_session()
        if Arbitrator().has_reached_max_attempts(session):
            Storage().set_state(StateEnum.LOST)
            return

        turn: Turn = Storage().get_current_turn()
        if Arbitrator().has_valid_combination(turn.get_feedback()):
            Storage().set_state(StateEnum.WON)
            return
