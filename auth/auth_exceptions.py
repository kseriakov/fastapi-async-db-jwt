from fastapi import HTTPException, status


class UnAuthorized(HTTPException):
    def __init__():
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
