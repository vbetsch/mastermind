from src.domain.usecases.continue_a_game import ContinueAGame
from src.domain.usecases.create_a_game import CreateAGame
from src.domain.usecases.show_leaderboard import ShowLeaderboard
from src.libs.communication.IMediator import IMediator
from src.libs.communication.Subscriber import Subscriber
from src.libs.options.aggregates.MainMenuOptionsList import MainMenuOptionsList


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.create_a_game = CreateAGame()
        self.continue_a_game = ContinueAGame()
        self.show_leaderboard = ShowLeaderboard()

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case MainMenuOptionsList.CREATE_A_GAME.name:
                self.create_a_game.execute()
            case MainMenuOptionsList.CONTINUE_A_GAME.name:
                self.continue_a_game.execute()
            case MainMenuOptionsList.SHOW_LEADERBOARD.name:
                self.show_leaderboard.execute()
            case MainMenuOptionsList.QUIT.name:
                self.send("EXIT")
            case _:
                raise Exception(f"Unknown choice: {message}")
