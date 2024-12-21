from typing import List
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.api.v1.models.base import OrmBase


class MShipment(OrmBase):
    __tablename__ = "shipments"
    
    created_at: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(datetime.timezone.utc),
        server_default=func.now())
    author: Mapped[str]
    total_price: Mapped[int]
    description: Mapped[str] = mapped_column(nullable=True)

    # goods: Mapped[List[""]]