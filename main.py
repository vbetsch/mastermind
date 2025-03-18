from src.app.controllers.MainMenuController import MainMenuController
from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.usecases.continue_a_game import ContinueAGame
from src.app.usecases.create_a_game import CreateAGame
from src.app.usecases.show_leaderboard import ShowLeaderboard
from src.common.abstract.IUseCase import IUseCase
from src.common.communication.Mediator import Mediator
from src.infra.repositories.SessionRepository import SessionRepository
from src.ui.cli.CLIController import CLIController


def inject_dependencies() -> CLIController:
    # Repositories
    session_repository: ISessionRepository = SessionRepository()

    # Use Cases
    create_a_game: IUseCase = CreateAGame(session_repository=session_repository)
    continue_a_game: IUseCase = ContinueAGame()
    show_leaderboard: IUseCase = ShowLeaderboard()

    # Communication
    mediator: Mediator = Mediator()
    cli: CLIController = CLIController(mediator=mediator)
    MainMenuController(
        mediator=mediator,
        create_a_game=create_a_game,
        continue_a_game=continue_a_game,
        show_leaderboard=show_leaderboard,
    )
    return cli


def run():
    cli: CLIController = inject_dependencies()
    cli.welcome()
    cli.main_menu()


if __name__ == '__main__':
    run()
