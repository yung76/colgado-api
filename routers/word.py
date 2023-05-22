from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends, Path, Query
from typing import Optional, List
from pydantic import BaseModel, Field
from config.database import Session
from models.user import User as UserModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.word import WordService
from schemas.word import Word

word_router = APIRouter()


#, dependencies=[Depends(JWTBearer())] esto es para solicitar token
@word_router.get('/words', tags=['word'], response_model=List[Word], status_code=200)
def get_words() -> List[Word]:
    db = Session()
    result = WordService(db).get_words()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@word_router.get('/word/{id}', tags=['word'], response_model=Word)
def get_words(id: int = Path(ge=1, le=2000)) -> Word:
    db = Session()
    result = WordService(db).get_word(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@word_router.post('/words', tags=['word'], response_model=dict, status_code=201)
def create_word(word: Word) -> dict:
    db = Session()
    WordService(db).create_word(word)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado una palabra"})


@word_router.put('/words/{id}', tags=['word'], response_model=dict, status_code=200)
def update_word(id: int, word: Word) -> dict:
    db = Session()
    result = WordService(db).get_word(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    WordService(db).update_word(id, word)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la palabra"})


@word_router.delete('/words/{id}', tags=['word'], response_model=dict, status_code=200)
def delete_word(id: int) -> dict:
    db = Session()
    result = WordService(db).get_word(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    WordService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la palabra"})
