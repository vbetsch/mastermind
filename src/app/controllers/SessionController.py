from src.app.controllers.IController import IController
from src.app.ports.usecases.session.ICreateSessionUseCase import ICreateSessionUseCase
from src.app.ports.usecases.session.IRunSessionUseCase import IRunSessionUseCase
from src.app.ports.usecases.session.IStopSessionUseCase import IStopSessionUseCase
from src.app.presenters.PlayerPresenter import PlayerPresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.decorators.dto.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.dto.check_dto_required_fields import check_dto_required_fields
from src.common.exceptions.DTOException import DTOException
from src.common.patterns.mediator.IMediator import IMediator


class SessionController(IController):
    def __init__(self, mediator: IMediator,
                 create_session: ICreateSessionUseCase,
                 run_session: IRunSessionUseCase,
                 stop_session: IStopSessionUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._create_session: ICreateSessionUseCase = create_session
        self._run_session: IRunSessionUseCase = run_session
        self._stop_session: IStopSessionUseCase = stop_session

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.CREATE_AND_RUN_SESSION.name:
                try:
                    self._handle_create_and_run_session(message, sender, dto)
                except DTOException:
                    return
            case EventEnum.STOP_SESSION.name:
                self._stop_session.execute()

    @check_dto_is_defined(EventEnum.CALLBACK_PREPARE, PlayerPresenter)
    @check_dto_required_fields(EventEnum.CALLBACK_PREPARE, PlayerPresenter)
    def _handle_create_and_run_session(self, message: str, sender: Subscriber, dto: PlayerPresenter = None) -> None:
        self._create_session.execute(dto.player)
        self._run_session.execute()
