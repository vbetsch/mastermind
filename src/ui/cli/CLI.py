from src.common.communication.Data import Data
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.Displayer import Displayer


class CLI(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        print(f"(02/04/2025 21:25) @reyks || CLI.py:11 || mediator || {mediator}")
        self.displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber, data: Data | None = None) -> None:
        match message:
            case EventEnum.SHOW_MAIN_MENU.name:
                self.main_menu()
            case EventEnum.SHOW_PLAY_MENU.name:
                self.play_menu()

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def start(self):
        self.welcome()
        self.main_menu()

    def main_menu(self) -> None:
        choice: EventEnum = self.displayer.show_main_menu()
        self.send(choice.name)

    def play_menu(self) -> None:
        print("Display play menu...")
        self.main_menu() # TODO: to delete

    def quit(self):
        self.send(EventEnum.STOP_SESSION.name)
        self.displayer.print_message("Good Bye!")
