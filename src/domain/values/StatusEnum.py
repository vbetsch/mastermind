from enum import Enum


class StatusEnum(Enum):
    NOT_STARTED: int = 0
    RUNNING: int = 1
    STOPPED: int = 2
    DONE: int = 3
