from src.common.communication.IMediator import IMediator
from src.common.communication.Subscriber import Subscriber
from src.common.messages.callbacks.UICallbackMessages import UICallbackMessages
from src.common.messages.menu.MenuOption import MenuOption
from src.ui.cli.Displayer import Displayer


class CLIController(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self.displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case UICallbackMessages.EXIT.name:
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
