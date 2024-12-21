from typing import Optional
from pydantic import BaseModel


class SUserBase(BaseModel):

    name: str
    password: str


class SUserCreate(SUserBase):
    pass


class SUserUpdatePartial(SUserCreate):
    name: Optional[str] = None
    password: Optional[str] = None


class SUser(SUserBase):
    
    id: int