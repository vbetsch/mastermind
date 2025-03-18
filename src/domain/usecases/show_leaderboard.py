from src.app.ports.IUseCase import IUseCase


class ShowLeaderboard(IUseCase):
    def execute(self) -> None:
        print("Showing leaderboard...")
