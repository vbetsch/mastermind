from peewee import SqliteDatabase

from src.common.decorators.Singleton import Singleton
from src.infra.database.models.SessionModel import SessionModel
from src.infra.env.EnvironmentConfig import EnvironmentConfig


@Singleton
class DatabaseConfig:
    def __init__(self):
        self._database_file_path = EnvironmentConfig().get_database_file_path()
        self._db = SqliteDatabase(self._database_file_path)
        self._tables = [SessionModel]
        self._db.bind(self._tables)
        self._create_tables()

    def _create_tables(self):
        self.connect()
        self._db.create_tables(self._tables)
        self.close()

    def db(self):
        return self._db

    def connect(self):
        self._db.connect()

    def close(self):
        self._db.close()
