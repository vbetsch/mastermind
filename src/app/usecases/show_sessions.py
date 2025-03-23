from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase


class ShowSessions(IMainMenuUseCase):
    def execute(self) -> None:
        print("Showing sessions...")
