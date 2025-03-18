from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

from src.app.controllers.MainMenuController import MainMenuController
from src.libs.abstract.IController import IController
from src.libs.callbacks.ICallback import ICallback
from src.libs.decorators.Singleton import Singleton
from src.libs.enums.OptionEnum import OptionEnum
from src.view.cli.components.Menu import Menu


@Singleton
class CLI:
    def __init__(self) -> None:
        self._console: Console = Console()
        self._ascii_font: str = "slant"
        self._main_menu: Menu = Menu(
            console=self._console,
            title="Main menu",
            options=[
                OptionEnum.CREATE_A_GAME,
                OptionEnum.CONTINUE_A_GAME,
                OptionEnum.SHOW_LEADERBOARD,
                OptionEnum.QUIT
            ])
        self.main_menu_controller: IController = MainMenuController()

    def _print_ascii_art(self, text: str) -> None:
        ascii_art = figlet_format(text, font=self._ascii_font)
        ascii_text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def _print_message(self, message: str, style=None) -> None:
        text = Text(message, style=style)
        self._console.print(text)

    def _handle_callbacks(self, callback: ICallback) -> None:
        match callback.name:
            case "QUIT":
                self.quit()
            case _:
                raise Exception(f"Unknown callback: {callback.name}")

    def welcome(self) -> None:
        self._print_message("Welcome to")
        self._print_ascii_art("mastermind")

    def show_main_menu(self) -> None:
        choice: OptionEnum = self._main_menu.show()
        callback: ICallback | None = self.main_menu_controller.handle(choice)
        if callback:
            self._handle_callbacks(callback)

    def quit(self):
        self._print_message("Good Bye!")
