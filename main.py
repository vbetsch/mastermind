from src.app.controllers.MainMenuController import MainMenuController
from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.IMainMenuUseCase import IMainMenuUseCase
from src.app.usecases.continue_a_session import ContinueASession
from src.app.usecases.create_a_session import CreateASession
from src.app.usecases.show_sessions import ShowSessions
from src.common.communication.Mediator import Mediator
from src.domain.entities.Player import Player
from src.infra.repositories.SessionRepository import SessionRepository
from src.ui.cli.CLI import CLI


def inject_dependencies() -> CLI:
    # Player
    player: Player = Player(name="default")

    # Repositories
    session_repository: ISessionRepository = SessionRepository()

    # Use Cases
    create_a_session: IMainMenuUseCase = CreateASession(
        player=player,
        session_repository=session_repository)
    continue_a_session: IMainMenuUseCase = ContinueASession()
    show_sessions: IMainMenuUseCase = ShowSessions()

    # Controllers
    mediator: Mediator = Mediator()
    cli: CLI = CLI(mediator=mediator)
    MainMenuController(
        mediator=mediator,
        create_a_session=create_a_session,
        continue_a_session=continue_a_session,
        show_sessions=show_sessions,
    )
    return cli


def run():
    cli: CLI = inject_dependencies()
    cli.welcome()
    cli.main_menu()

def cancel():
    cli: CLI = inject_dependencies()
    cli.quit()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        cancel()
