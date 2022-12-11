from fastapi import APIRouter, Depends, status

from user.security import get_current_user
from .schemas import PostCreate, PostShow, PostShowDetail
from . import service


router = APIRouter()


@router.get("/", response_model=list[PostShow])
async def post_list():
    return await service.get_post_list()


@router.get("/{id}", response_model=PostShowDetail)
async def post_detail(id: int):
    post = await service.get_post(id)
    owner = await service.get_owner_post(id)
    return PostShowDetail(**dict(post), owner=owner)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_create(item: PostCreate, user: str = Depends(get_current_user)):
    return await service.create_post(item, user)
