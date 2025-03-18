from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

from src.libs.decorators.Singleton import Singleton


@Singleton
class CLI:
    def __init__(self) -> None:
        self.console: Console = Console()
        self.ascii_font: str = "slant"

    def _print_ascii_art(self, text) -> None:
        ascii_art = figlet_format(text, font=self.ascii_font)
        ascii_text = Text(ascii_art, style="overline")
        self.console.print(ascii_text)

    def _print_message(self, message, style=None) -> None:
        text = Text(message, style=style)
        self.console.print(text)

    def welcome(self):
        self._print_message("Welcome to")
        self._print_ascii_art("mastermind")

