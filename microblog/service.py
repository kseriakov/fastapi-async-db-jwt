from core.db import database
from user.models import User
from user.service import get_user_by_id
from .models import Post, posts_table
from .schemas import PostCreate, PostShow


async def get_post(id: int):
    query = posts_table.select().where(posts_table.c.id == id)
    post = await database.fetch_one(query)
    return post


async def get_owner_post(id: int):
    query = posts_table.select().where(posts_table.c.id == id)
    post = await database.fetch_one(query)
    return await get_user_by_id(post.user_id)


async def get_post_list():
    query = posts_table.select()
    return await database.fetch_all(query)


async def create_post(data: PostCreate, user: User):
    query = posts_table.insert().values({**data.dict(), "user_id": user.id})
    return await database.execute(query)
