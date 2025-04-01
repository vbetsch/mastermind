from peewee import UUIDField

from src.infra.database.models.BaseModel import BaseModel


class HistoryModel(BaseModel):
    playerId = UUIDField(null=False)
    # sessions
