from src.ui.cli.Displayer import Displayer
from src.ui.cli.handlers.IHandler import IHandler


class CLI:
    def __init__(self, main_menu_handler: IHandler) -> None:
        self.displayer: Displayer = Displayer()
        self.main_menu_handler: IHandler = main_menu_handler

    def handle_callbacks(self, callback: str):
        match callback:
            case "SHOW_MAIN_MENU":
                self.main_menu()
            case "SHOW_PLAY_MENU":
                print("Display play menu...")
            case _:
                raise Exception(f"Unknown callback: {callback}")

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def main_menu(self) -> None:
        choice: str = self.displayer.show_main_menu()
        callback: str = self.main_menu_handler.manage(choice)
        self.handle_callbacks(callback)

    def quit(self):
        self.displayer.print_message("Good Bye!")
