from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase


class ContinueAGame(IMainMenuUseCase):
    def execute(self) -> None:
        print("Continuing game...")
