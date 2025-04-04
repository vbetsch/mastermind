from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.app.controllers.PlayerController import PlayerController
from src.app.controllers.PrepareController import PrepareController
from src.app.controllers.SessionController import SessionController
from src.app.usecases.player.get_player import GetPlayer
from src.app.usecases.prepare.get_available_colors import GetAvailableColors
from src.app.usecases.prepare.get_number_beads import GetBeadsPerCombination
from src.app.usecases.prepare.get_previous_proposals import GetPreviousProposals
from src.app.usecases.proposal.create_combination import CreateCombination
from src.app.usecases.session.create_session import CreateSession
from src.app.usecases.session.run_session import RunSession
from src.app.usecases.session.stop_session import StopSession
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler
from src.ui.cli.handlers.PlayMenuHandler import PlayMenuHandler


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
    get_available_colors = providers.Factory(GetAvailableColors)
    get_previous_proposals = providers.Factory(GetPreviousProposals)
    get_beads_per_combination = providers.Factory(GetBeadsPerCombination)

    # Proposal
    create_combination_factory = providers.Factory(
        CreateCombination,
        get_available_colors=get_available_colors,
    )
    create_combination = create_combination_factory()

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
    prepare_controller_factory = providers.Factory(
        PrepareController,
        mediator=mediator,
        get_available_colors=get_available_colors,
        get_previous_proposals=get_previous_proposals,
        get_beads_per_combination=get_beads_per_combination,
    )
    player_controller = player_controller_factory()
    session_controller = session_controller_factory()
    prepare_controller = prepare_controller_factory()

    # Handlers
    main_menu_handler_factory = providers.Factory(
        MainMenuHandler,
        mediator=mediator
    )
    play_menu_handler_factory = providers.Factory(
        PlayMenuHandler,
        mediator=mediator
    )
    main_menu_handler = main_menu_handler_factory()
    play_menu_handler = play_menu_handler_factory()

    # UI
    cli = providers.Factory(
        CLI,
        mediator=mediator
    )
