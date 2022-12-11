from fastapi import APIRouter

from microblog import blog
from user import user


routes = APIRouter()

routes.include_router(blog.router, prefix="/blog", tags=["Blog"])
routes.include_router(user.router, tags=["User"])
