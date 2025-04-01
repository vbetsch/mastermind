from src.app.controllers.SessionController import SessionController
from src.app.ports.repositories.IHistoryRepository import IHistoryRepository
from src.app.ports.repositories.IPlayerRepository import IPlayerRepository
from src.app.ports.repositories.ISessionRepository import ISessionRepository
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.app.ports.usecases.ISessionUseCase import ISessionUseCase
from src.app.usecases.create_session import CreateSession
from src.app.usecases.get_or_create_player import GetOrCreatePlayer
from src.app.usecases.run_session import RunSession
from src.app.usecases.stop_session import StopSession
from src.common.communication.Mediator import Mediator
from src.infra.repositories.HistoryRepository import HistoryRepository
from src.infra.repositories.PlayerRepository import PlayerRepository
from src.infra.repositories.SessionRepository import SessionRepository
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler


def inject_dependencies() -> CLI:
    # Mediator
    mediator: Mediator = Mediator()

    # Repositories
    player_repository: IPlayerRepository = PlayerRepository()
    history_repository: IHistoryRepository = HistoryRepository()
    session_repository: ISessionRepository = SessionRepository()

    # Use Cases
    get_or_create_player: IPlayerUseCase = GetOrCreatePlayer(
        history_repository=history_repository,
        player_repository=player_repository,
    )
    create_session: ISessionUseCase = CreateSession(
        session_repository=session_repository,
    )
    run_session: ISessionUseCase = RunSession(
        session_repository=session_repository,
    )
    stop_session: ISessionUseCase = StopSession(
        session_repository=session_repository,
    )

    # Controllers
    SessionController(
        mediator=mediator,
        get_or_create_player=get_or_create_player,
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
