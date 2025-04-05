from src.app.ports.usecases.state.IGetState import IGetState
from src.domain.core.Arbitrator import Arbitrator
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.sessions.Turn import Turn
from src.domain.values.stages.StateEnum import StateEnum


class GetState(IGetState):
    def execute(self) -> StateEnum:
        session: Session = Storage().get_current_session()
        state: StateEnum = StateEnum.PLAYING
        if Arbitrator().has_reached_max_attempts(session):
            state = StateEnum.LOST

        turn: Turn = Storage().get_current_turn()
        if Arbitrator().has_valid_combination(turn.get_feedback()):
            state = StateEnum.WON

        Storage().set_state(state)
        return state
