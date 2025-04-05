from src.app.controllers.IController import IController
from src.app.data.UpdateTurnData import UpdateTurnData
from src.app.ports.usecases.turn import IRunTurn
from src.app.ports.usecases.turn.ICreateTurn import ICreateTurn
from src.app.ports.usecases.turn.IStopTurn import IStopTurn
from src.app.ports.usecases.turn.IUpdateTurn import IUpdateTurn
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.decorators.dto.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.dto.check_dto_required_fields import check_dto_required_fields
from src.common.patterns.mediator.IMediator import IMediator


class TurnController(IController):
    def __init__(self, mediator: IMediator,
                 create_turn: ICreateTurn,
                 run_turn: IRunTurn,
                 update_turn: IUpdateTurn,
                 stop_turn: IStopTurn,
                 close_turn: IStopTurn):
        super().__init__(self.__class__.__name__, mediator)
        self._create_turn: ICreateTurn = create_turn
        self._run_turn: IRunTurn = run_turn
        self._update_turn: IUpdateTurn = update_turn
        self._stop_turn: IStopTurn = stop_turn
        self._close_turn: IStopTurn = close_turn

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_TURN.name:
                self._create_turn.execute()
                self._run_turn.execute()
            case EventEnum.UPDATE_AND_CLOSE_TURN.name:
                self._handle_update_and_close_turn(dto)
            case EventEnum.STOP_TURN.name:
                self._stop_turn.execute()

    @check_dto_is_defined(EventEnum.UPDATE_AND_CLOSE_TURN, UpdateTurnData)
    @check_dto_required_fields(EventEnum.UPDATE_AND_CLOSE_TURN, UpdateTurnData)
    def _handle_update_and_close_turn(self, dto: UpdateTurnData = None) -> None:
        self._update_turn.execute(feedback=dto.feedback, proposal=dto.proposal)
        self._close_turn.execute()
