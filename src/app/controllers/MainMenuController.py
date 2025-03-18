from src.libs.abstract.IController import IController
from src.libs.callbacks.ICallback import ICallback
from src.libs.callbacks.UICallback import UICallback
from src.libs.enums.OptionEnum import OptionEnum


class MainMenuController(IController):
    def handle(self, choice: OptionEnum) -> ICallback | None:
        match choice:
            case OptionEnum.CREATE_A_GAME:
                print("Creating a new game...")
            case OptionEnum.CONTINUE_A_GAME:
                print("Continuing game...")
            case OptionEnum.SHOW_LEADERBOARD:
                print("Showing leaderboard...")
            case OptionEnum.QUIT:
                return UICallback("QUIT")
            case _:
                raise Exception(f"Unknown choice: {choice}")
