from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.app.controllers.PlayerController import PlayerController
from src.app.controllers.SessionController import SessionController
from src.app.usecases.create_session import CreateSession
from src.app.usecases.get_player import GetPlayer
from src.app.usecases.run_session import RunSession
from src.app.usecases.stop_session import StopSession
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler


class Container(DeclarativeContainer):
    mediator: Mediator = Mediator()

    # Use Cases
    get_player = providers.Factory(GetPlayer)
    create_session = providers.Factory(CreateSession)
    run_session = providers.Factory(RunSession)
    stop_session = providers.Factory(StopSession)

    # Controllers
    factory = providers.Factory(
        PlayerController,
        mediator=mediator,
        get_player=get_player
    )
    player_controller = factory()

    factory = providers.Factory(
        SessionController,
        mediator=mediator,
        create_session=create_session,
        run_session=run_session,
        stop_session=stop_session
    )
    session_controller = factory()

    # Handlers
    factory = providers.Factory(
        MainMenuHandler,
        mediator=mediator
    )
    main_menu_handler = factory()

    # UI
    cli = providers.Factory(
        CLI,
        mediator=mediator
    )
