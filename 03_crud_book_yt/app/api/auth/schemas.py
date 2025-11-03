from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    identifier: str
    password: str


class UserRegisterSchema(BaseModel):
    username: str
    email: str
    password: str

