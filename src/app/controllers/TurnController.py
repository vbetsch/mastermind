from src.app.controllers.IController import IController
from src.common.communication.Subscriber import Subscriber
from src.common.communication.dto.IDto import IDto
from src.common.patterns.mediator.IMediator import IMediator


class TurnController(IController):
    def __init__(self, mediator: IMediator):
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber, dto: IDto = None) -> None:
        pass
        # match message:
        #     case EventEnum.CREATE_AND_RUN_TURN.name:
        #         pass
