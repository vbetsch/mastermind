import pytest
from unittest.mock import MagicMock

from src.domain.entities.Player import Player
from src.domain.entities.Session import Session
from src.domain.values.StatusEnum import StatusEnum
from src.domain.values.combinations.Combination import Combination
from src.domain.values.sessions.SessionMemento import SessionMemento
from src.domain.values.sessions.Turn import Turn


class TestSession:
    @pytest.fixture
    def player(self):
        return MagicMock(spec=Player)

    @pytest.fixture
    def combination(self):
        return MagicMock(spec=Combination)

    @pytest.fixture
    def session(self, player, combination):
        return Session(player=player, secret_combination=combination)

    def test_init(self, session, player, combination):
        assert session.player == player
        assert session.secret_combination == combination
        assert session.status == StatusEnum.NOT_STARTED
        assert session.turns == []

    def test_run(self, session):
        session.run()
        assert session.status == StatusEnum.RUNNING

    def test_save(self, session):
        memento = session.save()
        assert isinstance(memento, SessionMemento)

    def test_restore(self, session, player, combination):
        modified_session = Session(
            player=player,
            secret_combination=combination,
            status=StatusEnum.RUNNING,
            turns=[MagicMock(spec=Turn)]
        )

        mock_memento = MagicMock(spec=SessionMemento)
        mock_memento.get_saved_state.return_value = modified_session

        restored_session = session.restore(mock_memento)

        assert restored_session.status == StatusEnum.RUNNING
        assert len(restored_session.turns) == 1
        assert restored_session.player == player
        assert restored_session.secret_combination == combination

        mock_memento.get_saved_state.assert_called_once()

    def test_stop(self, session):
        session.stop()
        assert session.status == StatusEnum.STOPPED
