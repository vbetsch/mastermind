from peewee import Model, AutoField


class BaseModel(Model):
    id: AutoField = AutoField()
