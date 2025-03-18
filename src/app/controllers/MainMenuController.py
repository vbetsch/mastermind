from src.app.exceptions.NotHandledException import NotHandledException
from src.app.usecases.continue_a_game import ContinueAGame
from src.app.usecases.create_a_game import CreateAGame
from src.app.usecases.show_leaderboard import ShowLeaderboard
from src.common.communication.IMediator import IMediator
from src.common.communication.Subscriber import Subscriber
from src.common.messages.cli.menu.MainMenuOptions import MainMenuOptions
from src.common.messages.controllers.ControllerMessages import ControllerMessages


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_a_game = CreateAGame()
        self.continue_a_game = ContinueAGame()
        self.show_leaderboard = ShowLeaderboard()

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
