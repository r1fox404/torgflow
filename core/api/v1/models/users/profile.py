from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.api.v1.models.base import OrmBase


if TYPE_CHECKING:
    from .user import MUser


class MProfile(OrmBase):
    __tablename__ = "profiles"
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]
    
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspaces.id"))
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["MUser"] = relationship(back_populates="profile")
    
    shipments: Mapped[List["1"]] = mapped_column(nullable=True)
