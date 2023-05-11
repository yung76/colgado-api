from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.user import user_router
from routers.auth import auth_router
from routers.save import save_router

app = FastAPI()
app.title = "Colgado API"

app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(save_router)


Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
