# Pydantic
from pydantic import BaseModel


class UserLogin(BaseModel):
    name: str
    password: str


class UserRegister(UserLogin):
    age: int


class UserOut(BaseModel):
    id_: str
    name: str
    age: int
    token: str

    def __str__(self):
        return self.name
