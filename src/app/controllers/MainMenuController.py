from src.domain.usecases.continue_a_game import ContinueAGame
from src.domain.usecases.create_a_game import CreateAGame
from src.domain.usecases.show_leaderboard import ShowLeaderboard
from src.libs.communication.IMediator import IMediator
from src.libs.communication.Subscriber import Subscriber
from src.libs.options.callbacks.UICallbackOptions import UICallbackOptions
from src.libs.options.menu.MainMenuOptions import MainMenuOptions


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
                self.send(UICallbackOptions.EXIT.name)
            case _:
                raise Exception(f"Unknown choice: {message}")
