from enum import Enum


class StateEnum(Enum):
    INSIDE_MENUS: str = 0
    PLAYING: str = 1
    WON: str = 2
    LOST: str = 3
