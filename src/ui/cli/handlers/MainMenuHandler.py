from src.common.communication.Subscriber import Subscriber
from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class MainMenuHandler(IHandler):
    def __init__(self, mediator: IMediator):
        super().__init__(self.__class__.__name__, mediator)

    def handle(self, message: str, sender: Subscriber) -> None:
        match message:
            case "CREATE_A_SESSION":
                self.send("CREATE_AND_RUN_SESSION")
                self.send("SHOW_PLAY_MENU")
