from src.app.data.StateData import StateData
from src.app.presenters.IPresenter import IPresenter
from src.common.communication.OutcomeEnum import OutcomeEnum
from src.common.dto.OutcomeDTO import OutcomeDTO
from src.domain.values.stages.StateEnum import StateEnum


class StatePresenter(IPresenter):
    def __init__(self, data: StateData):
        super().__init__(data)
        self.data: StateData = data

    def present(self) -> OutcomeDTO:
        match self.data.state:
            case StateEnum.WON:
                return OutcomeDTO(OutcomeEnum.VICTORY)
            case StateEnum.LOST:
                return OutcomeDTO(OutcomeEnum.DEFEAT)
            case _:
                return OutcomeDTO(OutcomeEnum.TRY_AGAIN)
