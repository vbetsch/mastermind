from src.libs.communication.IMediator import IMediator
from src.libs.communication.Subscriber import Subscriber
from src.libs.options.aggregates.MainMenuOptionsList import MainMenuOptionsList


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case MainMenuOptionsList.CREATE_A_GAME.name:
                print("Creating a new game...")
            case MainMenuOptionsList.CONTINUE_A_GAME.name:
                print("Continuing game...")
            case MainMenuOptionsList.SHOW_LEADERBOARD.name:
                print("Showing leaderboard...")
            case MainMenuOptionsList.QUIT.name:
                self.send("EXIT")
            case _:
                raise Exception(f"Unknown choice: {message}")
