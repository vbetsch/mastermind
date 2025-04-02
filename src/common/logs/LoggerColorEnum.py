from enum import Enum


class LoggerColorEnum(Enum):
    RESET = "\033[0m"
    ERROR = "\033[1;31m"
    WARNING = "\033[1;33m"
    SUCCESS = "\033[1;32m"
    INFO = "\033[1;34m"
    DEBUG = "\033[1;37m"
