from fastapi import APIRouter
from starlette.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

auth_router = APIRouter()


@auth_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
