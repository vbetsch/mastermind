from enum import Enum


class EventEnum(Enum):
    # --- Display ---
    SHOW_MAIN_MENU: str = "Main menu"
    SHOW_PLAY_MENU: str = "Play menu"
    SHOW_FEEDBACK: str = "Show feedback"
    ASK_PROPOSAL: str = "Make a proposal"
    CANCEL: str = "Cancel"

    # --- Handlers ---
    # Main menu
    NEW_GAME: str = "New game"
    QUIT: str = "Quit"

    # Play menu
    PLAY: str = "Play"
    STOP: str = "Stop"

    # --- Callbacks ---
    CALLBACK_PREPARE: str = "CALLBACK PREPARE"
    REPLY_PROPOSAL: str = "REPLY_PROPOSAL"
    OUTCOME: str = "OUTCOME"

    # --- Backend ---
    GET_PLAYER: str = "GET_PLAYER"
    PREPARE: str = "PREPARE"
    SEND_PROPOSAL: str = "SEND_PROPOSAL"
    CREATE_AND_RUN_SESSION: str = "CREATE_AND_RUN_SESSION"
    STOP_SESSION: str = "STOP_SESSION"
    CREATE_AND_RUN_TURN: str = "CREATE_AND_RUN_TURN"
    UPDATE_AND_CLOSE_TURN: str = "UPDATE_AND_CLOSE_TURN"
    STOP_TURN: str = "STOP_TURN"
    END_TURN: str = "END_TURN"
