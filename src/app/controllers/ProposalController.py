from src.app.controllers.IController import IController
from src.app.data.FeedbackData import FeedbackData
from src.app.data.UpdateTurnData import UpdateTurnData
from src.app.ports.usecases.proposal.ICreateCombination import ICreateCombination
from src.app.ports.usecases.proposal.IGenerateFeedback import IGenerateFeedback
from src.app.presenters.FeedbackPresenter import FeedbackPresenter
from src.common.communication.EventEnum import EventEnum
from src.common.communication.Subscriber import Subscriber
from src.common.decorators.func.check_dto_is_defined import check_dto_is_defined
from src.common.decorators.func.check_dto_required_fields import check_dto_required_fields
from src.common.dto.IDto import IDto
from src.common.dto.ProposalDTO import ProposalDTO
from src.common.patterns.mediator.IMediator import IMediator


class ProposalController(IController):
    def __init__(self, mediator: IMediator,
                 create_combination: ICreateCombination,
                 generate_feedback: IGenerateFeedback):
        super().__init__(self.__class__.__name__, mediator)
        self._create_combination: ICreateCombination = create_combination
        self._generate_feedback: IGenerateFeedback = generate_feedback

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        match message:
            case EventEnum.SEND_PROPOSAL.name:
                self._handle_send_proposal(dto)

    @check_dto_is_defined(EventEnum.SEND_PROPOSAL, ProposalDTO)
    @check_dto_required_fields(EventEnum.SEND_PROPOSAL, ProposalDTO)
    def _handle_send_proposal(self, dto: ProposalDTO = None) -> None:
        combination = self._create_combination.execute(dto.proposal)
        feedback = self._generate_feedback.execute(combination)
        presenter: FeedbackPresenter = FeedbackPresenter(FeedbackData(feedback))
        self.send(EventEnum.REPLY_PROPOSAL.name, presenter.present())
        self.send(EventEnum.UPDATE_AND_CLOSE_TURN.name,
                  UpdateTurnData(feedback=feedback, proposal=combination))
