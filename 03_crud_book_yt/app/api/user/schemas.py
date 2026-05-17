from pydantic import BaseModel


class UserUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    Address: str
