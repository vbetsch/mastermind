from src.app.ports.usecases.prepare.IGetPreviousProposals import IGetPreviousProposals
from src.common.logs.Logger import Logger
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.combinations.Combination import Combination


class GetPreviousProposals(IGetPreviousProposals):
    def execute(self) -> list[Combination]:
        session: Session = Storage().get_current_session()

        previous_proposals: list[Combination] = []
        for turn in session.turns:
            proposal: Combination | None = turn.get_if_proposal()
            if proposal:
                previous_proposals.append(proposal)

        return previous_proposals
