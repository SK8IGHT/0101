from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Excavation(BaseModelModify):
    date_start: str
    date_end: str
    place_id: int
    user_id: int


class Place(BaseModelModify):
    name: str


class Artifact(BaseModelModify):
    name: str
    age: int
    culture_id: int


class Culture(BaseModelModify):
    name: str


class User(BaseModelModify):
    name: str
    password: str
    post: str


class UserAuth(BaseModel):
    name: str
    password: str

