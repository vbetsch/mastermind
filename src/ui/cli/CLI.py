from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.exceptions.CallbackException import CallbackException
from src.common.patterns.mediator.IMediator import IMediator
from src.domain.core.Generator import Generator
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
            case EventEnum.ASK_PROPOSAL.name:
                if not data or not isinstance(data, PrepareDTO) or data.all_colors is None or data.previous_proposals is None:
                    raise CallbackException("Callback prepare doesn't have data")
                # TODO: self.ask_proposal(data.all_colors, data.previous_proposals)
                self.ask_proposal(data.all_colors, [str(Generator().generate_combination()), str(Generator().generate_combination()), str(Generator().generate_combination())])
            case EventEnum.CANCEL.name:
                self.cancel()

    def welcome(self) -> None:
        self._displayer.print_message("Welcome to")
        self._displayer.print_ascii_art("mastermind")

    def start(self) -> None:
        self.welcome()
        self.main_menu()

    def main_menu(self) -> None:
        choice: EventEnum = self._displayer.show_main_menu()
        self.send(choice.name)

    def play_menu(self) -> None:
        choice: EventEnum = self._displayer.show_play_menu()
        self.send(choice.name)

    def ask_proposal(self, all_colors: dict[str, str], previous_proposals: list[str]) -> None:
        if len(previous_proposals) > 0:
            self._displayer.print_list("Previous attempts :", previous_proposals)

        self._displayer.print_list("All colors available :", all_colors, are_colors=True)
        self._displayer.jump_lines(1)
        proposal: str = self._displayer.ask_string(EventEnum.ASK_PROPOSAL.value)

    def cancel(self) -> None:
        self.send(EventEnum.STOP_SESSION.name)
        self._displayer.jump_lines(2)
        self._displayer.print_message("Good Bye!")
