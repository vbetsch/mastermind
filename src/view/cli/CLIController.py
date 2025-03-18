from src.libs.enums.OptionEnum import OptionEnum
from src.libs.mediators.IMediator import IMediator
from src.libs.mediators.Subscriber import Subscriber
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
        choice: OptionEnum = self.displayer.show_main_menu()
        self.send(choice.name)

    def quit(self):
        self.displayer.print_message("Good Bye!")
