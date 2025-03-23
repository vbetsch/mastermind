from os import getenv

from src.common.decorators.Singleton import Singleton
from dotenv import load_dotenv


@Singleton
class EnvironmentHandler:
    def __init__(self):
        load_dotenv()

    def get_database_file_path(self) -> str:
        return getenv("DATABASE_FILE_PATH") or 'mastermind.db'
