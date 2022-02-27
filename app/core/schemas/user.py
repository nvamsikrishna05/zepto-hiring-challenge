from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    user_name: str
    is_admin: bool

    class Config:
        orm_mode = True
