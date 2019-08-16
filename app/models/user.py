from pydantic import BaseModel


class User(BaseModel):
    username: str

class UserInRequest(User):
    password: str