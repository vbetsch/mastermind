from src.app.ports.usecases.prepare.IGetPreviousProposals import IGetPreviousProposals
from src.common.logs.Logger import Logger
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.combinations.Combination import Combination


class GetPreviousProposals(IGetPreviousProposals):
    def execute(self) -> list[str]:
        session: Session = Storage().get_current_session()

        Logger().info(f"The secret combination is {session.secret_combination}")

        previous_proposals: list[str] = []
        for turn in session.turns:
            proposal: Combination | None = turn.get_if_proposal()
            if proposal:
                previous_proposals.append(str(proposal))

        return previous_proposals
