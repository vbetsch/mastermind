from src.common.patterns.mediator.IMediator import IMediator
from src.ui.cli.handlers.IHandler import IHandler


class MainMenuHandler(IHandler):
    def __init__(self, mediator: IMediator):
        super().__init__(self.__class__.__name__, mediator)

    def manage(self, message: str) -> str:
        match message:
            case "CREATE_A_SESSION":
                self.send("CREATE_AND_RUN_SESSION")
                return "SHOW_PLAY_MENU"
            case _:
                raise Exception(f"Unknown message: {message}")
