from typing import Optional
from pydantic import BaseModel


class SShipment(BaseModel):
    
    author: str
    total_price: int
    description: Optional[str]