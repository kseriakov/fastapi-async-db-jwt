# Чтобы alembic отслеживал модели, их надо импортировать вместе с Base
# И отсюда Base импортируется в env.py

from .db import Base
from microblog.models import Post
from user.models import User
