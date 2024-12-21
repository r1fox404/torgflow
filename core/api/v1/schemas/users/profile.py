from typing import Optional
from pydantic import BaseModel


class SProfileBase(BaseModel):
    
    first_name: str
    last_name: str
    email: str
    role: str = "manager"
    workspace_id: int
    user_id: int


class SProfileCreate(SProfileBase):
    pass


class SProfileUpdatePartial(SProfileCreate):
    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    workspace_id: Optional[int] = None


class SProfile(SProfileBase):
    
    id: int
    shipments: Optional["SShipment"] = []
