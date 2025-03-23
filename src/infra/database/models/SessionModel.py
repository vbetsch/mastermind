from peewee import CharField, IntegerField

from src.infra.database.models.BaseModel import BaseModel


class SessionModel(BaseModel):
    status = CharField()
