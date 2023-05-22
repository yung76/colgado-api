from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends, Path, Query
from typing import Optional, List
from pydantic import BaseModel, Field
from config.database import Session
from models.user import User as UserModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.user import UserService
from schemas.user import User

user_router = APIRouter()


#, dependencies=[Depends(JWTBearer())] esto es para solicitar token
@user_router.get('/users', tags=['users'], response_model=List[User], status_code=200)
def get_users() -> List[User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.get('/user/{id}', tags=['users'], response_model=User)
def get_users(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post('/users', tags=['users'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un usuario"})


@user_router.put('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    UserService(db).update_movie(id, user)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


@user_router.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_user(id: int) -> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado "})
    UserService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
