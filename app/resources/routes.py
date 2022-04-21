# FastAPI
from fastapi import APIRouter

# Resources
from . import users


api_router = APIRouter()
api_router.include_router(users.router)
