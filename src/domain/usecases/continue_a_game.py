from src.app.ports.IUseCase import IUseCase


class ContinueAGame(IUseCase):
    def execute(self) -> None:
        print("Continuing game...")
