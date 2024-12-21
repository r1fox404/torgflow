from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.api.v1.models.base import OrmBase


class MProduct(OrmBase):
    __tablename__ = "products"
    
    name: Mapped[str]
    price: Mapped[int]
    color: Mapped[str] = mapped_column(nullable=True)
    imei: Mapped[str] = mapped_column(nullable=True)
    serial_number: Mapped[str] = mapped_column(nullable=True)
    memory: Mapped[int] = mapped_column(nullable=True)
    carrier: Mapped[str] = mapped_column(nullable=True)
    count: Mapped[int] = mapped_column(nullable=True)
    
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))