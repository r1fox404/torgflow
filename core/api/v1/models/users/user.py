from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.api.v1.models.base import OrmBase


if TYPE_CHECKING:
    from .profile import MProfile


class MUser(OrmBase):
    __tablename__ = "users"
    
    username: Mapped[str]
    password: Mapped[str]
    
    profile: Mapped["MProfile"] = relationship(back_populates="user")