from src.app.ports.IUseCase import IUseCase


class CreateAGame(IUseCase):
    def execute(self) -> None:
        print("Creating a new game...")
