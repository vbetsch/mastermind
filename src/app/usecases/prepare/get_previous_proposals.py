from src.app.ports.usecases.prepare.IGetPreviousProposals import IGetPreviousProposals
from src.common.logs.Logger import Logger
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class GetPreviousProposals(IGetPreviousProposals):

    def execute(self) -> list[str]:
        session: Session = Storage().get_current_session()
        Logger().info(f"The secret combination is {session.get_secret_combination()}")
        return session.get_previous_proposals()
