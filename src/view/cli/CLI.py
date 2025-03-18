from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

from src.libs.decorators.Singleton import Singleton
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
                "Create a game",
                "Continue a game",
                "Show leaderboard",
                "Quit"
            ])

    def _print_ascii_art(self, text: str) -> None:
        ascii_art = figlet_format(text, font=self._ascii_font)
        ascii_text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def _print_message(self, message: str, style=None) -> None:
        text = Text(message, style=style)
        self._console.print(text)

    def welcome(self) -> None:
        self._print_message("Welcome to")
        self._print_ascii_art("mastermind")

    def show_main_menu(self) -> None:
        choice = self._main_menu.show()
