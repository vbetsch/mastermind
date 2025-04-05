from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.app.controllers.PlayerController import PlayerController
from src.app.controllers.PrepareController import PrepareController
from src.app.controllers.ProposalController import ProposalController
from src.app.controllers.SessionController import SessionController
from src.app.controllers.StateController import StateController
from src.app.controllers.StatsController import StatsController
from src.app.controllers.TurnController import TurnController
from src.app.usecases.player.get_player import GetPlayer
from src.app.usecases.prepare.get_available_colors import GetAvailableColors
from src.app.usecases.prepare.get_number_beads import GetBeadsPerCombination
from src.app.usecases.prepare.get_previous_proposals import GetPreviousProposals
from src.app.usecases.proposal.create_combination import CreateCombination
from src.app.usecases.proposal.generate_feedback import GenerateFeedback
from src.app.usecases.session.create_session import CreateSession
from src.app.usecases.session.end_session import EndSession
from src.app.usecases.session.run_session import RunSession
from src.app.usecases.session.stop_session import StopSession
from src.app.usecases.state.get_state import GetState
from src.app.usecases.stats.get_stats import GetStats
from src.app.usecases.turn.close_turn import CloseTurn
from src.app.usecases.turn.create_turn import CreateTurn
from src.app.usecases.turn.run_turn import RunTurn
from src.app.usecases.turn.stop_turn import StopTurn
from src.app.usecases.turn.update_turn import UpdateTurn
from src.common.communication.Mediator import Mediator
from src.ui.cli.CLI import CLI
from src.ui.cli.handlers.MainMenuHandler import MainMenuHandler
from src.ui.cli.handlers.OutcomeHandler import OutcomeHandler
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
    end_session = providers.Factory(EndSession)

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
    generate_feedback = providers.Factory(GenerateFeedback)

    # Turn
    create_turn = providers.Factory(CreateTurn)
    run_turn = providers.Factory(RunTurn)
    update_turn = providers.Factory(UpdateTurn)
    stop_turn = providers.Factory(StopTurn)
    close_turn = providers.Factory(CloseTurn)

    # State
    get_state = providers.Factory(GetState)

    # Stats
    get_stats = providers.Factory(GetStats)

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
        stop_session=stop_session,
        end_session=end_session,
    )
    prepare_controller_factory = providers.Factory(
        PrepareController,
        mediator=mediator,
        get_available_colors=get_available_colors,
        get_previous_proposals=get_previous_proposals,
        get_beads_per_combination=get_beads_per_combination,
    )
    proposal_controller_factory = providers.Factory(
        ProposalController,
        mediator=mediator,
        create_combination=create_combination,
        generate_feedback=generate_feedback,
    )
    turn_controller_factory = providers.Factory(
        TurnController,
        mediator=mediator,
        create_turn=create_turn,
        run_turn=run_turn,
        update_turn=update_turn,
        stop_turn=stop_turn,
        close_turn=close_turn,
    )
    state_controller_factory = providers.Factory(
        StateController,
        mediator=mediator,
        get_state=get_state,
    )
    stats_controller_factory = providers.Factory(
        StatsController,
        mediator=mediator,
        get_stats=get_stats,
    )
    player_controller = player_controller_factory()
    session_controller = session_controller_factory()
    prepare_controller = prepare_controller_factory()
    proposal_controller = proposal_controller_factory()
    turn_controller = turn_controller_factory()
    state_controller = state_controller_factory()
    stats_controller = stats_controller_factory()

    # Handlers
    main_menu_handler_factory = providers.Factory(
        MainMenuHandler,
        mediator=mediator
    )
    play_menu_handler_factory = providers.Factory(
        PlayMenuHandler,
        mediator=mediator
    )
    outcome_handler_factory = providers.Factory(
        OutcomeHandler,
        mediator=mediator
    )
    main_menu_handler = main_menu_handler_factory()
    play_menu_handler = play_menu_handler_factory()
    outcome_handler = outcome_handler_factory()

    # UI
    cli = providers.Factory(
        CLI,
        mediator=mediator
    )
