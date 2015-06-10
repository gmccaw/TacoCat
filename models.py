from peewee import *

DATABASE = SqliteDatabase('tacocat.db')


class User(Model):
    email = TextField(unique=True)
    password = TextField

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, password, email):
        password = password
        email = email


class Taco(Model):
    protein = TextField
    shell = TextField
    cheese = BooleanField
    extras = TextField

    class Meta:
        database = DATABASE