from enum import Enum


class EventEnum(Enum):
    # Display
    SHOW_MAIN_MENU = "Main menu"
    SHOW_PLAY_MENU = "Play menu"

    # Handlers
    CREATE_A_SESSION = "New game"

    # Back
    CREATE_AND_RUN_SESSION = 1
