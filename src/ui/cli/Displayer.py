from pyfiglet import figlet_format, FigletString
from rich.console import Console
from rich.prompt import Prompt
from rich.style import Style
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
        self._play_menu: Menu = Menu(
            console=self._console,
            title=EventEnum.SHOW_PLAY_MENU.value,
            options=[
                EventEnum.PLAY,
                EventEnum.STOP,
            ]
        )

    def _print_bullet_points_for_list(self, elements: list, are_colors: bool = False):
        if are_colors:
            for element in elements:
                self._console.print(f"- [{element}]{element}[/]")
        else:
            for element in elements:
                self._console.print(f"- {element}")
        pass

    def _print_bullet_points_for_dict(self, elements: dict, are_colors: bool = False):
        if are_colors:
            for key, value in elements.items():
                self._console.print(f"- [{value}]{key} = {value}[/]")
        else:
            for key, value in elements.items():
                self._console.print(f"- {key} = {value}")

    def jump_lines(self, number: int) -> None:
        if number < 1:
            raise Exception('Line breaks cannot be less than 1')
        self._console.print("\n" * number)

    def print_ascii_art(self, text: str) -> None:
        ascii_art: FigletString = figlet_format(text, font=self._ascii_font)
        ascii_text: Text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def print_message(self, message: str, style: str | Style = None) -> None:
        text: Text = Text(message, style=style)
        self._console.print(text)

    def print_bullet_points(self, elements: list | dict, are_colors: bool = False) -> None:
        if isinstance(elements, list):
            self._print_bullet_points_for_list(elements, are_colors)
        elif isinstance(elements, dict):
            self._print_bullet_points_for_dict(elements, are_colors)

    @staticmethod
    def ask_string(label: str, style: str = None) -> str:
        if style:
            return Prompt.ask(f"[{style}]{label}[/]")
        else:
            return Prompt.ask(label)

    def print_list(self, title: str, elements: list[str] | dict, are_colors: bool = False) -> None:
        self.jump_lines(1)
        self.print_message(title)
        self.print_bullet_points(elements, are_colors=are_colors)

    def show_main_menu(self) -> EventEnum:
        return self._main_menu.show()

    def show_play_menu(self) -> EventEnum:
        return self._play_menu.show()
