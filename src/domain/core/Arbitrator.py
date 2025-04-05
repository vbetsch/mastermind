from src.app.exceptions.ProposalException import ProposalException
from src.common.decorators.Singleton import Singleton
from src.domain.core.Rules import Rules
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session
from src.domain.values.combinations.Bead import Bead
from src.domain.values.combinations.Combination import Combination
from src.domain.values.turns.Feedback import Feedback


@Singleton
class Arbitrator:
    @staticmethod
    def has_right_length(proposal: str) -> bool:
        if len(proposal) != Rules().get_beads_per_combination():
            raise ProposalException(f"Proposal {proposal} has wrong length")
        return True

    @staticmethod
    def has_only_available_colors(proposal: str, available_colors: dict[str, str]) -> bool:
        for char in proposal:
            if not char.upper() in available_colors.keys():
                raise ProposalException(f"Proposal {proposal} has unavailable color")
        return True

    @staticmethod
    def has_valid_combination(feedback: Feedback) -> bool:
        if feedback.get_red_indicator_value() == Rules().get_beads_per_combination():
            return True
        return False

    @staticmethod
    def has_reached_max_attempts(session: Session) -> bool:
        return session.get_turns_length() >= Rules().get_max_attempts_before_loose()

    @staticmethod
    def _has_bead(bead: Bead, combination: Combination) -> bool:
        return bead.get_color_key() in combination.get_list_bead_color_keys()

    @staticmethod
    def _have_same_color_in_same_place(combination_a: Combination, combination_b: Combination, index) -> bool:
        return combination_a.get_bead_color_key(index) == combination_b.get_bead_color_key(index)

    def _calculate_right_colors_in_right_places(self, secret_combination: Combination, proposal: Combination) -> int:
        nb_beads: int = Rules().get_beads_per_combination()
        result: int = 0
        for index in range(nb_beads):
            if self._have_same_color_in_same_place(
                    secret_combination,
                    proposal,
                    index):
                result += 1
        return result

    def _calculate_right_colors_in_wrong_places(self, secret_combination: Combination, proposal: Combination) -> int:
        result: int = 0
        for index, bead in enumerate(proposal.get_beads()):
            if (self._has_bead(bead=bead, combination=secret_combination)
                    and not self._have_same_color_in_same_place(
                        secret_combination,
                        proposal,
                        index)):
                result += 1
        return result

    def generate_feedback(self, proposal: Combination) -> Feedback:
        feedback: Feedback = Feedback()
        secret_combination: Combination = Storage().get_current_secret_combination()
        feedback.set_red_indicator_value(
            self._calculate_right_colors_in_right_places(
                secret_combination=secret_combination,
                proposal=proposal
            )
        )
        feedback.set_white_indicator_value(
            self._calculate_right_colors_in_wrong_places(
                secret_combination=secret_combination,
                proposal=proposal
            )
        )
        return feedback
