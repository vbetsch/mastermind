from src.app.controllers.PlayerController import PlayerController
from src.app.controllers.SessionController import SessionController
from src.app.ports.usecases.ICreateSessionUseCase import ICreateSessionUseCase
from src.app.ports.usecases.IPlayerUseCase import IPlayerUseCase
from src.app.ports.usecases.IRunSessionUseCase import IRunSessionUseCase
from src.app.ports.usecases.IStopSessionUseCase import IStopSessionUseCase
from src.app.usecases.create_session import CreateSession
from src.app.usecases.get_player import GetPlayer
from src.app.usecases.run_session import RunSession
from src.app.usecases.stop_session import StopSession
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler


def inject_dependencies() -> CLI:
    # Mediator
    mediator: Mediator = Mediator()

    # Repositories

    # Use Cases
    get_player: IPlayerUseCase = GetPlayer()
    create_session: ICreateSessionUseCase = CreateSession()
    run_session: IRunSessionUseCase = RunSession()
    stop_session: IStopSessionUseCase = StopSession()

    # Controllers
    PlayerController(
        mediator=mediator,
        get_player=get_player,
    )
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
