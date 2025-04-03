from pyfiglet import figlet_format, FigletString
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
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

    def jump_lines(self, number: int) -> None:
        if number < 1:
            raise Exception('Line breaks cannot be less than 1')
        self._console.print("\n" * number)

    def print_ascii_art(self, text: str) -> None:
        ascii_art: FigletString = figlet_format(text, font=self._ascii_font)
        ascii_text: Text = Text(ascii_art, style="bold")
        self._console.print(ascii_text)

    def print_message(self, message: str, style=None) -> None:
        text: Text = Text(message, style=style)
        self._console.print(text)

    def print_bullet_points(self, elements: list) -> None:
        markdown_text = "".join(f"- {key}\n" for key in elements)
        self._console.print(Markdown(markdown_text))

    @staticmethod
    def ask_choices(label: str, choices: list[str], style: str = None) -> str:
        if style:
            return Prompt.ask(f"[{style}]{label}[/]", choices=choices)
        else:
            return Prompt.ask(label, choices=choices)

    def show_main_menu(self) -> EventEnum:
        return self._main_menu.show()

    def show_play_menu(self) -> EventEnum:
        return self._play_menu.show()
