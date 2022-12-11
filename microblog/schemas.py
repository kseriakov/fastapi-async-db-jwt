from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int
    date: datetime


class PostCreate(PostBase):
    pass
