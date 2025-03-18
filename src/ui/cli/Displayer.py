from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

from src.libs.options.menu.MainMenuOptions import MainMenuOptions
from src.libs.options.menu.MenuOption import MenuOption
from src.ui.cli.components.Menu import Menu


class Displayer:
    def __init__(self) -> None:
        self._console: Console = Console()
        self._ascii_font: str = "slant"

    def print_ascii_art(self, text: str) -> None:
        ascii_art = figlet_format(text, font=self._ascii_font)
        ascii_text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def print_message(self, message: str, style=None) -> None:
        text = Text(message, style=style)
        self._console.print(text)

    def show_main_menu(self) -> MenuOption:
        main_menu: Menu = Menu(
            console=self._console,
            title="Main menu",
            options=MainMenuOptions.all_options()
        )
        return main_menu.show()
