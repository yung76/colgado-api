from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from typing import Optional, List
from services.save import SaveService
from utils.jwt_manager import create_token
from schemas.save import Save
from config.database import Session

save_router = APIRouter()


@save_router.get('/saves', tags=['save'], response_model=List[Save], status_code=200)
def get_saves() -> List[Save]:
    db = Session()
    result = SaveService(db).get_saves()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@save_router.post('/saves', tags=['save'], response_model=dict, status_code=201)
def create_save(save: Save) -> dict:
    db = Session()
    SaveService(db).create_save(save)
    return JSONResponse(status_code=201, content={"message": "Se ha guardado la partida"})

