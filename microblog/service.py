from core.db import database
from .models import posts_table
from .schemas import PostCreate


async def get_post_list():
    query = posts_table.select()
    return await database.fetch_all(query)


async def create_post(data: PostCreate):
    query = posts_table.insert().values(**data.dict())
    return await database.execute(query)
