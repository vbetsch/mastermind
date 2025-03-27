from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.Displayer import Displayer


class CLI(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case "SHOW_MAIN_MENU":
                self.main_menu()
            case "SHOW_PLAY_MENU":
                print("Display play menu...")

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def main_menu(self) -> None:
        choice: str = self.displayer.show_main_menu()
        self.send(choice)

    def quit(self):
        self.displayer.print_message("Good Bye!")
