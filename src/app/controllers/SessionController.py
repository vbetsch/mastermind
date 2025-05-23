from src.app.controllers.IController import IController
from src.app.data.PlayerData import PlayerData
from src.app.ports.usecases.session.ICreateSessionUseCase import ICreateSessionUseCase
from src.app.ports.usecases.session.IEndSession import IEndSession
from src.app.ports.usecases.session.IRunSessionUseCase import IRunSessionUseCase
from src.app.ports.usecases.session.IStopSessionUseCase import IStopSessionUseCase
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.decorators.func.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.func.check_dto_required_fields import check_dto_required_fields
from src.common.dto.IDto import IDto
from src.common.exceptions.DTOException import DTOException
from src.common.patterns.mediator.IMediator import IMediator


class SessionController(IController):
    def __init__(self, mediator: IMediator,
                 create_session: ICreateSessionUseCase,
                 run_session: IRunSessionUseCase,
                 stop_session: IStopSessionUseCase,
                 end_session: IEndSession) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._create_session: ICreateSessionUseCase = create_session
        self._run_session: IRunSessionUseCase = run_session
        self._stop_session: IStopSessionUseCase = stop_session
        self._end_session: IEndSession = end_session

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_SESSION.name:
                try:
                    self._handle_create_and_run_session(dto)
                except DTOException:
                    return
            case EventEnum.STOP_SESSION.name:
                self._stop_session.execute()
            case EventEnum.VICTORY.name:
                self._handle_victory_or_defeat()
            case EventEnum.DEFEAT.name:
                self._handle_victory_or_defeat()

    @check_dto_is_defined(EventEnum.CALLBACK_PREPARE, PlayerData)
    @check_dto_required_fields(EventEnum.CALLBACK_PREPARE, PlayerData)
    def _handle_create_and_run_session(self, dto: PlayerData = None) -> None:
        self._create_session.execute(dto.player)
        self._run_session.execute()

    def _handle_victory_or_defeat(self):
        self._end_session.execute()
