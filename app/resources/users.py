# FastAPI
from fastapi import APIRouter, Depends

# Schemas
from app.schemas import UserRegister, UserOut

# Database
from app.database import users_collection

# JWT
from fastapi_jwt_auth import AuthJWT

# Crypt
from passlib.context import CryptContext


router = APIRouter(tags=['Users'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('/users/register/', response_model=UserOut)
async def create_user(user: UserRegister, Authorize: AuthJWT = Depends()):
    token = Authorize.create_access_token(subject=user.name, expires_time=False)
    user.password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict['token'] = token
    user_id = users_collection.insert_one(user_dict).inserted_id
    user_dict.pop('password')
    user_dict['id_'] = str(user_id)
    return user_dict
