from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from auth.auth_exceptions import UnAuthorized
from auth.auth_jwt import Jwt
from settings import TOKEN_URL
from . import service


auth_jwt = Jwt()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = auth_jwt.verify_token(token)
    username = payload.sub

    if not username:
        raise UnAuthorized()

    user = await service.get_user(username)

    if not user:
        raise UnAuthorized()

    return user
