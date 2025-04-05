from src.app.data.StatsData import StatsData
from src.app.presenters.IPresenter import IPresenter
from src.common.communication.OutcomeEnum import OutcomeEnum
from src.common.dto.StatsDTO import StatsDTO
from src.domain.values.stages.StateEnum import StateEnum


class StatsPresenter(IPresenter):
    def __init__(self, data: StatsData):
        super().__init__(data)
        self.data: StatsData = data

    def present(self) -> StatsDTO:
        outcome: OutcomeEnum = OutcomeEnum.TRY_AGAIN
        match self.data.state:
            case StateEnum.WON:
                outcome = OutcomeEnum.VICTORY
            case StateEnum.LOST:
                outcome = OutcomeEnum.DEFEAT
        return StatsDTO(
            outcome=outcome,
            attempts_number=self.data.attempts_number
        )
