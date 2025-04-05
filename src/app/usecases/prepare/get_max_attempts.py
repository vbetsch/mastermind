from src.app.data.MaxAttemptsData import MaxAttemptsData
from src.app.ports.usecases.prepare.IGetMaxAttempts import IGetMaxAttempts
from src.domain.core.Rules import Rules


class GetMaxAttempts(IGetMaxAttempts):
    def execute(self) -> MaxAttemptsData:
        max_attempts: int = Rules().get_max_attempts_before_loose()
        return MaxAttemptsData(max_attempts)
