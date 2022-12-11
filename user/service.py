from core.db import database
from .schemas import UserCreate
from .models import users_table


async def get_user(username: str):
    query = users_table.select().where(users_table.c.name == username)
    return await database.fetch_one(query)


async def get_user_by_id(id: int):
    query = users_table.select().where(users_table.c.id == id)
    return await database.fetch_one(query)


async def create_user(data: UserCreate):
    query = users_table.insert().values(**data.dict())
    return await database.execute(query)
