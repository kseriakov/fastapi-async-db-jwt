import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://blog:123@localhost/blog"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
