from enum import Enum


class EventEnum(Enum):
    # Display
    SHOW_MAIN_MENU: str = "Main menu"
    SHOW_PLAY_MENU: str = "Play menu"

    # Handlers
    NEW_GAME: str = "New game"

    # Back
    GET_PLAYER: str = "GET_PLAYER"
    CREATE_AND_RUN_SESSION: str = "CREATE_AND_RUN_SESSION"
    STOP_SESSION: str = "STOP_SESSION"
