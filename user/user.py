from asyncpg import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth.schemas import TokensResponse
from settings import TOKEN_URL
from .models import User
from .security import auth_jwt
from .schemas import UserCreate
from . import service

router = APIRouter()


@router.post(path="/" + TOKEN_URL, response_model=TokensResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username, password = form_data.username, form_data.password
    user: User = await service.get_user(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with username '{username}' not register",
        )

    tokens = auth_jwt.get_tokens(username, password, user.password)

    return TokensResponse(**tokens.dict(), token_type="bearer")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: UserCreate):
    payload = data.dict()
    payload.update(
        {"password": auth_jwt.get_password_hash(payload["password"])}
    )
    try:
        user_id = await service.create_user(UserCreate(**payload))
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with same username/email already exists",
        )
    return user_id
 