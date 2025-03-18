from src.app.exceptions.NotHandledException import NotHandledException
from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase
from src.common.communication.IMediator import IMediator
from src.common.communication.Subscriber import Subscriber
from src.common.communication.messages.cli.menu.MainMenuOptions import MainMenuOptions
from src.common.communication.messages.controllers.ControllerMessages import ControllerMessages


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator, create_a_game: IMainMenuUseCase, continue_a_game: IMainMenuUseCase,
                 show_leaderboard: IMainMenuUseCase) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_a_game: IMainMenuUseCase = create_a_game
        self.continue_a_game: IMainMenuUseCase = continue_a_game
        self.show_leaderboard: IMainMenuUseCase = show_leaderboard

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case MainMenuOptions.CREATE_A_GAME.name:
                self.create_a_game.execute()
            case MainMenuOptions.CONTINUE_A_GAME.name:
                self.continue_a_game.execute()
            case MainMenuOptions.SHOW_LEADERBOARD.name:
                self.show_leaderboard.execute()
            case MainMenuOptions.QUIT.name:
                self.send(ControllerMessages.EXIT.name)
            case _:
                raise NotHandledException()
