from src.app.controllers.SessionController import SessionController
from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.app.usecases.create_session import CreateSession
from src.app.usecases.run_session import RunSession
from src.app.usecases.stop_session import StopSession
from src.common.communication.Mediator import Mediator
from src.domain.entities.Player import Player
from src.infra.repositories.SessionRepository import SessionRepository
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler


def inject_dependencies() -> CLI:
    # Mediator
    mediator: Mediator = Mediator()

    # Player
    player: Player = Player(name="default")

    # Repositories
    session_repository: ISessionRepository = SessionRepository()

    # Use Cases
    create_session: ISessionUseCase = CreateSession(
        player=player,
        session_repository=session_repository,
    )
    run_session: ISessionUseCase = RunSession(
        player=player,
        session_repository=session_repository,
    )
    stop_session: ISessionUseCase = StopSession(
        player=player,
        session_repository=session_repository,
    )

    # Controllers
    SessionController(
        mediator=mediator,
        create_session=create_session,
        run_session=run_session,
        stop_session=stop_session
    )

    # Handlers
    MainMenuHandler(mediator=mediator)

    return CLI(mediator=mediator)


def run():
    cli: CLI = inject_dependencies()
    cli.start()


def cancel():
    cli: CLI = inject_dependencies()
    cli.quit()


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        cancel()
