from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.FeedbackDTO import FeedbackDTO
from src.common.communication.dto.IDto import IDto
from src.common.communication.dto.PrepareDTO import PrepareDTO
from src.common.communication.dto.ProposalDTO import ProposalDTO
from src.common.communication.dto.StatsDTO import StatsDTO
from src.common.communication.dto.enums.OutcomeEnum import OutcomeEnum
from src.common.decorators.dto.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.dto.check_dto_required_fields import check_dto_required_fields
from src.common.logs.Logger import Logger
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.Displayer import Displayer


class CLI(Subscriber):
    def __init__(self, mediator: IMediator) -> None:
        super().__init__(self.__class__.__name__, mediator)
        self._displayer: Displayer = Displayer()

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.SHOW_MAIN_MENU.name:
                self.main_menu()
            case EventEnum.SHOW_PLAY_MENU.name:
                self.play_menu()
            case EventEnum.ASK_PROPOSAL.name:
                self._handle_ask_proposal(dto)
            case EventEnum.SHOW_FEEDBACK.name:
                self._handle_show_feedback(dto)
            case EventEnum.DISPLAY_STATS.name:
                self._handle_display_stats(dto)
            case EventEnum.CANCEL.name:
                self.cancel()

    @check_dto_is_defined(EventEnum.ASK_PROPOSAL, PrepareDTO)
    @check_dto_required_fields(EventEnum.ASK_PROPOSAL, PrepareDTO)
    def _handle_ask_proposal(self, dto: PrepareDTO = None) -> None:
        self.ask_proposal(dto)

    @check_dto_is_defined(EventEnum.SHOW_FEEDBACK, FeedbackDTO)
    @check_dto_required_fields(EventEnum.SHOW_FEEDBACK, FeedbackDTO)
    def _handle_show_feedback(self, dto: FeedbackDTO = None) -> None:
        self.show_feedback(dto)

    @check_dto_is_defined(EventEnum.DISPLAY_STATS, StatsDTO)
    @check_dto_required_fields(EventEnum.DISPLAY_STATS, StatsDTO)
    def _handle_display_stats(self, dto: StatsDTO = None) -> None:
        self.display_stats(dto)

    @staticmethod
    def _has_right_length(proposal: str, beads_per_combination: int) -> bool:
        if len(proposal) != beads_per_combination:
            Logger().error(f"The proposal must be {beads_per_combination} characters long")
            return False
        return True

    @staticmethod
    def _has_only_available_colors(proposal: str, available_colors: dict[str, str]) -> bool:
        for char in proposal:
            if not char.upper() in available_colors.keys():
                Logger().error(f"The proposal must only has available colors")
                return False
        return True

    def _ask_proposal_until_have_valid(self, dto: PrepareDTO):
        proposal: str = ""
        has_right_length: bool = False
        has_only_available_colors: bool = False
        while not has_right_length or not has_only_available_colors:
            proposal = self._displayer.ask_string(EventEnum.ASK_PROPOSAL.value)
            has_right_length = False
            has_only_available_colors = False

            if self._has_right_length(proposal, dto.beads_per_combination):
                has_right_length = True

            if self._has_only_available_colors(proposal, dto.available_colors):
                has_only_available_colors = True
        self.send(EventEnum.SEND_PROPOSAL.name, ProposalDTO(proposal))

    def _display_previous_attempts_and_available_colors(self, dto: PrepareDTO):
        if len(dto.previous_proposals) > 0:
            self._displayer.print_list("Previous attempts :", dto.previous_proposals)

        self._displayer.print_list("All colors available :", dto.available_colors, are_colors=True)
        self._displayer.jump_lines(1)

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

    def ask_proposal(self, dto: PrepareDTO) -> None:
        self._display_previous_attempts_and_available_colors(dto)
        self._ask_proposal_until_have_valid(dto)

    def show_feedback(self, dto: FeedbackDTO) -> None:
        self._displayer.print_list("Feedback :", dto.feedback)

    def display_stats(self, dto: StatsDTO) -> None:
        match dto.outcome:
            case OutcomeEnum.VICTORY:
                self._displayer.print_message(f"Victory !!!")
            case OutcomeEnum.DEFEAT:
                self._displayer.print_message(f"Defeat :(")
        self._displayer.print_message(f"You've made {dto.attempts_number} attempts")

    def cancel(self) -> None:
        self.send(EventEnum.STOP_TURN.name)
        self.send(EventEnum.STOP_SESSION.name)
        self._displayer.jump_lines(1)
        self._displayer.print_message("Good Bye!")
