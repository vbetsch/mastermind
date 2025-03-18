from src.libs.enums.OptionEnum import OptionEnum
from src.libs.communication.IMediator import IMediator
from src.libs.communication.Subscriber import Subscriber


class MainMenuController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case OptionEnum.CREATE_A_GAME.name:
                print("Creating a new game...")
            case OptionEnum.CONTINUE_A_GAME.name:
                print("Continuing game...")
            case OptionEnum.SHOW_LEADERBOARD.name:
                print("Showing leaderboard...")
            case OptionEnum.QUIT.name:
                self.send("EXIT")
            case _:
                raise Exception(f"Unknown choice: {message}")
