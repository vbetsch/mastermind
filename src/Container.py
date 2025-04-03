from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.app.controllers.PlayerController import PlayerController
from src.app.controllers.SessionController import SessionController
from src.app.usecases.player.get_player import GetPlayer
from src.app.usecases.prepare.get_previous_proposals import GetPreviousProposals
from src.app.usecases.session.create_session import CreateSession
from src.app.usecases.session.run_session import RunSession
from src.app.usecases.session.stop_session import StopSession
from src.app.usecases.values.get_all_colors import GetAllColors
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler


class Container(DeclarativeContainer):
    mediator: Mediator = Mediator()

    # --- Use Cases ---
    # Player
    get_player = providers.Factory(GetPlayer)

    # Sessions
    create_session = providers.Factory(CreateSession)
    run_session = providers.Factory(RunSession)
    stop_session = providers.Factory(StopSession)

    # Prepare
    get_all_colors = providers.Factory(GetAllColors)
    get_previous_proposals = providers.Factory(GetPreviousProposals)

    # --- Controllers ---
    player_controller_factory = providers.Factory(
        PlayerController,
        mediator=mediator,
        get_player=get_player
    )
    session_controller_factory = providers.Factory(
        SessionController,
        mediator=mediator,
        create_session=create_session,
        run_session=run_session,
        stop_session=stop_session
    )
    player_controller = player_controller_factory()
    session_controller = session_controller_factory()

    # Handlers
    main_menu_handler_factory = providers.Factory(
        MainMenuHandler,
        mediator=mediator
    )
    main_menu_handler = main_menu_handler_factory()

    # UI
    cli = providers.Factory(
        CLI,
        mediator=mediator
    )
