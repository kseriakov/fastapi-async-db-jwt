from sqlalchemy import Boolean, Column, Integer, String, DateTime, Table
from sqlalchemy.sql import func

from core.db import Base


class User(Base):
    __tablename__ = "microblog_user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, server_default="True")
    is_admin = Column(Boolean, server_default="False")


users_table: Table = User.__table__