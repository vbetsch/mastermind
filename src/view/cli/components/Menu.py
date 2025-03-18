from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from src.libs.enums.OptionEnum import OptionEnum


class Menu:
    def __init__(self, console: Console, title: str, options: list[OptionEnum]) -> None:
        self._console: Console = console
        self._title: str = title
        self._options: list[OptionEnum] = options

    def _render_columns(self, table: Table) -> None:
        table.add_column("Number", style="bold cyan", justify="center")
        table.add_column("Label")

    def _render_options(self, table: Table) -> None:
        for i, option in enumerate(self._options, start=1):
            table.add_row(str(i), option.value)

    def _render_table(self) -> Table:
        table = Table(title=self._title, header_style="bold magenta", show_header=False)
        self._render_columns(table)
        self._render_options(table)
        return table

    def _show_table(self) -> None:
        self._console.print(self._render_table())

    def _render_choices(self) -> list[str]:
        return [str(i + 1) for i in range(len(self._options))]

    def _ask_option(self) -> str:
        choice: str = Prompt.ask("[bold yellow]Choose an option[/]", choices=self._render_choices())

        if int(choice) < 1 or int(choice) > len(self._options):
            raise IndexError

        selected_option: OptionEnum = self._options[int(choice) - 1]
        if not selected_option:
            raise IndexError
        return selected_option.name

    def show(self) -> str:
        self._show_table()
        return self._ask_option()
