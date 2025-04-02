from peewee import CharField

from src.infra.database.models.BaseModel import BaseModel


class SessionModel(BaseModel):
    status: CharField = CharField(null=False)
