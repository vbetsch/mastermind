from src.app.controllers.MainMenuController import MainMenuController
from src.libs.abstract.IController import IController
from src.libs.callbacks.ICallback import ICallback
from src.libs.enums.OptionEnum import OptionEnum
from src.view.cli.Displayer import Displayer


class CLIController:
    def __init__(self) -> None:
        self.displayer = Displayer()
        self.main_menu_controller: IController = MainMenuController()

    def _handle_callbacks(self, callback: ICallback) -> None:
        match callback.name:
            case "QUIT":
                self.quit()
            case _:
                raise Exception(f"Unknown callback: {callback.name}")

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def main_menu(self) -> None:
        choice: OptionEnum = self.displayer.show_main_menu()
        callback: ICallback | None = self.main_menu_controller.handle(choice)
        if callback:
            self._handle_callbacks(callback)

    def quit(self):
        self.displayer.print_message("Good Bye!")
