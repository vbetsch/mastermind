from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase


class ShowGames(IMainMenuUseCase):
    def execute(self) -> None:
        print("Showing games...")
