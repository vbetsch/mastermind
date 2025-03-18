from src.common.abstract.IUseCase import IUseCase


class ShowLeaderboard(IUseCase):
    def execute(self) -> None:
        print("Showing leaderboard...")
