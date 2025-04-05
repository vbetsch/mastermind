from src.app.data.StatsData import StatsData
from src.app.ports.usecases.stats.IGetStats import IGetStats
from src.domain.core.Storage import Storage
from src.domain.entities.Session import Session


class GetStats(IGetStats):
    def execute(self) -> StatsData:
        session: Session = Storage().get_current_session()
        return StatsData(
            state=Storage().get_state(),
            attempts_number=session.get_turns_length()
        )
