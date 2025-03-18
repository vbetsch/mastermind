from src.common.abstract.IUseCase import IUseCase


class ContinueAGame(IUseCase):
    def execute(self) -> None:
        print("Continuing game...")
