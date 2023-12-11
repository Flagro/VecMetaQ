from decouple import config


SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")
