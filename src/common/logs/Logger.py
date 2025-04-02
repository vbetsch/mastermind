from src.common.decorators.Singleton import Singleton
from src.common.logs.LoggerColorEnum import LoggerColorEnum


@Singleton
class Logger:
    def __init__(self) -> None:
        self._prefix = "➔"

    def _print(self, tag: str, message: str, color: LoggerColorEnum = None, with_line_break: bool = False) -> None:
        content: str = f"{self._prefix} {tag}: {message}"
        if color:
            print(f"{'\n' if with_line_break else ''}{color.value}{content}{LoggerColorEnum.RESET.value}")
        else:
            print(f"{'\n' if with_line_break else ''}{content}")

    def log(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="LOG",
            message=message,
            with_line_break=line_break
        )

    def debug(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="DEBUG",
            message=message,
            color=LoggerColorEnum.DEBUG,
            with_line_break=line_break
        )

    def info(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="INFO",
            message=message,
            color=LoggerColorEnum.INFO,
            with_line_break=line_break
        )

    def warn(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="WARN",
            message=message,
            color=LoggerColorEnum.WARNING,
            with_line_break=line_break
        )

    def error(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="ERROR",
            message=message,
            color=LoggerColorEnum.ERROR,
            with_line_break=line_break
        )

    def critical(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="CRITICAL",
            message=message,
            color=LoggerColorEnum.ERROR,
            with_line_break=line_break
        )

    def ok(self, message: str, line_break: bool = False) -> None:
        self._print(
            tag="OK",
            message=message,
            color=LoggerColorEnum.SUCCESS,
            with_line_break=line_break
        )

    def done(self, line_break: bool = False) -> None:
        self.ok(
            message="Done",
            line_break=line_break
        )
