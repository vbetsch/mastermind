from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase


class ContinueASession(IMainMenuUseCase):
    def execute(self) -> None:
        print("Continuing game...")
