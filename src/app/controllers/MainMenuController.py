from src.app.exceptions.NotHandledException import NotHandledException
from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase
from src.common.communication.Subscriber import Subscriber
from src.common.communication.events.cli.menu.MainMenuOptions import MainMenuOptions
from src.common.communication.events.controllers.ControllerEvents import ControllerEvents
from src.common.patterns.mediator.IMediator import IMediator


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator, create_a_session: IMainMenuUseCase, continue_a_session: IMainMenuUseCase,
                 show_sessions: IMainMenuUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_a_session: IMainMenuUseCase = create_a_session
        self.continue_a_session: IMainMenuUseCase = continue_a_session
        self.show_sessions: IMainMenuUseCase = show_sessions

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case MainMenuOptions.CREATE_A_SESSION.name:
                self.create_a_session.execute()
                self.send(ControllerEvents.MAIN_MENU.name)
            case MainMenuOptions.CONTINUE_A_SESSION.name:
                self.continue_a_session.execute()
                self.send(ControllerEvents.MAIN_MENU.name)
            case MainMenuOptions.SHOW_SESSIONS.name:
                self.show_sessions.execute()
                self.send(ControllerEvents.MAIN_MENU.name)
            case MainMenuOptions.QUIT.name:
                self.send(ControllerEvents.EXIT.name)
            case _:
                raise NotHandledException()
