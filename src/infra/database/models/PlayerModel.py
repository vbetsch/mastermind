from peewee import CharField, ForeignKeyField

from src.infra.database.models.BaseModel import BaseModel
from src.infra.database.models.HistoryModel import HistoryModel


class PlayerModel(BaseModel):
    name = CharField(null=False, unique=True)
    state = CharField(null=False)
    history = ForeignKeyField(HistoryModel, unique=True, null=False)
