from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.Displayer import Displayer


class CLI(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber, data: IDto = None) -> None:
        match message:
            case EventEnum.SHOW_MAIN_MENU.name:
                self.main_menu()
            case EventEnum.SHOW_PLAY_MENU.name:
                self.play_menu()
            case EventEnum.CANCEL.name:
                self.cancel()

    def welcome(self) -> None:
        self._displayer.print_message("Welcome to")
        self._displayer.print_ascii_art("mastermind")

    def start(self):
        self.welcome()
        self.main_menu()

    def main_menu(self) -> None:
        choice: EventEnum = self._displayer.show_main_menu()
        self.send(choice.name)

    def play_menu(self) -> None:
        choice: EventEnum = self._displayer.show_play_menu()
        self.send(choice.name)

    def cancel(self):
        self.send(EventEnum.STOP_SESSION.name)
        self._displayer.print_message("Good Bye!", jump_lines=2)
