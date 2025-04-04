from src.app.controllers.IController import IController
from src.app.ports.usecases.turn import IRunTurn
from src.app.ports.usecases.turn.ICreateTurn import ICreateTurn
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator


class TurnController(IController):
    def __init__(self, mediator: IMediator,
                 create_turn: ICreateTurn,
                 run_turn: IRunTurn):
        super().__init__(self.__class__.__name__, mediator)
        self._create_turn: ICreateTurn = create_turn
        self._run_turn: IRunTurn = run_turn

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_TURN.name:
                self._create_turn.execute()
                self._run_turn.execute()
