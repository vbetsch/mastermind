from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase


class ShowLeaderboard(IMainMenuUseCase):
    def execute(self) -> None:
        print("Showing leaderboard...")
