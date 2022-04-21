# Utils
from decouple import config

# FastAPI
from fastapi import FastAPI

# Router
from .resources.routes import api_router

# JWT
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

app = FastAPI()
app.include_router(api_router)


#JWT Settings
class Settings(BaseModel):
    authjwt_secret_key: str = config('JWT_SECRET_KEY')


@AuthJWT.load_config
def get_config():
    return Settings()
