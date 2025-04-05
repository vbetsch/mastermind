from src.app.controllers.IController import IController
from src.app.data.StateData import StateData
from src.app.ports.usecases.state.IGetState import IGetState
from src.app.presenters.StatePresenter import StatePresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator


class StateController(IController):
    def __init__(self, mediator: IMediator,
                 get_state: IGetState):
        super().__init__(self.__class__.__name__, mediator)
        self._get_state: IGetState = get_state

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.END_TURN.name:
                state = self._get_state.execute()
                presenter: StatePresenter = StatePresenter(StateData(state))
                self.send(EventEnum.OUTCOME.name, presenter.present())
