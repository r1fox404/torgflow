from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship

from core.api.v1.models.base import OrmBase


if TYPE_CHECKING:
    from .product import MProduct


class MCategory(OrmBase):
    __tablename__ = "categories"
    
    name: Mapped[str]
    products: Mapped[List["MProduct"]] = relationship()