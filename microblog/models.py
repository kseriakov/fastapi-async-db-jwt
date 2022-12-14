from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.sql import func
from sqlalchemy.orm import backref, relationship

from core.db import Base


class Post(Base):

    __tablename__ = "microblog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("microblog_user.id"))
    owner = relationship("User", back_populates="posts")
    parent_id = Column(Integer, ForeignKey("microblog_posts.id"))
    children = relationship("Post", backref=backref("parent", remote_side=[id]))


#  Получаем экземпляр Table, для работы с databases, т.к. там только ORM
posts_table: Table = Post.__table__