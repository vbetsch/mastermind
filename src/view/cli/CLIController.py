from src.libs.enums.MainMenuOptionEnum import MainMenuOptionEnum
from src.libs.communication.IMediator import IMediator
from src.libs.communication.Subscriber import Subscriber
from src.view.cli.Displayer import Displayer


class CLIController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case "EXIT":
                self.quit()
            case _:
                raise Exception(f"Unknown message: {message}")

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def main_menu(self) -> None:
        choice: MainMenuOptionEnum = self.displayer.show_main_menu()
        self.send(choice.name)

    def quit(self):
        self.displayer.print_message("Good Bye!")
