from pyfiglet import figlet_format, FigletString
from rich.console import Console
from rich.text import Text

from src.common.communication.EventEnum import EventEnum
from src.ui.cli.components.Menu import Menu


class Displayer:
    def __init__(self) -> None:
        self._console: Console = Console()
        self._ascii_font: str = "slant"
        self._main_menu: Menu = Menu(
            console=self._console,
            title=EventEnum.SHOW_MAIN_MENU.value,
            options=[
                EventEnum.NEW_GAME,
                EventEnum.QUIT,
            ],
        )

    def print_ascii_art(self, text: str) -> None:
        ascii_art: FigletString = figlet_format(text, font=self._ascii_font)
        ascii_text: Text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def print_message(self, message: str, style=None, jump_lines: int = None) -> None:
        text: Text = Text(f"{'\n' * jump_lines if jump_lines else ''}{message}", style=style)
        self._console.print(text)

    def show_main_menu(self) -> EventEnum:
        return self._main_menu.show()
