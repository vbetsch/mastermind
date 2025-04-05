from src.common.decorators.Singleton import Singleton


@Singleton
class Rules:
    def __init__(self) -> None:
        self._dev_mode: bool = False  # Display logs and secret combination (default: False)
        self._save_when_played: bool = False  # Auto-save (default: False)
        self._beads_per_combination: int = 4  # Combinations length (default: 4)
        self._max_attempts_before_loose: int = 12  # Board size (default: 12)

    def get_dev_mode(self) -> bool:
        return self._dev_mode

    def get_save_when_played(self) -> bool:
        return self._save_when_played

    def get_beads_per_combination(self) -> int:
        return self._beads_per_combination

    def get_max_attempts_before_loose(self) -> int:
        return self._max_attempts_before_loose
