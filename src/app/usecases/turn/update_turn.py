from src.app.ports.usecases.turn.IUpdateTurn import IUpdateTurn
from src.common.logs.Logger import Logger
from src.domain.core.Storage import Storage
from src.domain.values.combinations.Combination import Combination
from src.domain.values.sessions.Turn import Turn
from src.domain.values.turns.Feedback import Feedback


class UpdateTurn(IUpdateTurn):
    def execute(self, feedback: Feedback, proposal: Combination) -> None:
        turn: Turn = Storage().get_current_turn()
        turn.set_feedback(feedback)
        turn.set_proposal(proposal)
        Storage().set_current_turn(turn)
        Logger().log("Turn updated", line_break=True)
