from src.common.communication.Subscriber import Subscriber
from src.common.communication.messages.cli.menu.MenuOption import MenuOption
from src.common.communication.messages.controllers.ControllerMessages import ControllerMessages
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.Displayer import Displayer


class CLIController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case ControllerMessages.MAIN_MENU.name:
                self.main_menu()
            case ControllerMessages.EXIT.name:
                self.quit()
            case _:
                raise Exception(f"Unknown message: {message}")

    def welcome(self) -> None:
        self.displayer.print_message("Welcome to")
        self.displayer.print_ascii_art("mastermind")

    def main_menu(self) -> None:
        choice: MenuOption = self.displayer.show_main_menu()
        self.send(choice.name)

    def quit(self):
        self.displayer.print_message("Good Bye!")
