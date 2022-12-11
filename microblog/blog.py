from fastapi import APIRouter, Depends, status

from user.security import get_current_user, oauth2_scheme
from .schemas import PostCreate, PostList
from . import service


router = APIRouter()


@router.get("/", response_model=list[PostList])
async def post_list():
    return await service.get_post_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_create(item: PostCreate, user: str = Depends(get_current_user)):
    return await service.create_post(item)
