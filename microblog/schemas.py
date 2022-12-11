from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from user.schemas import UserShow


class PostBase(BaseModel):
    title: str
    text: str
    parent_id: Optional[int]

    class Config:
        orm_mode = True


class PostShow(PostBase):
    id: int
    date: datetime
    user_id: Optional[int]
    
class PostShowDetail(PostBase):
    id: int
    date: datetime
    owner: Optional[UserShow]   


class PostCreate(PostBase):
    pass
