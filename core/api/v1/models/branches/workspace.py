from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.api.v1.models.base import OrmBase


if TYPE_CHECKING:
    from core.api.v1.models.users.profile import MProfile


class MWorkspace(OrmBase):
    __tablename__ = "workspaces"
    
    name: Mapped[str]
    adress: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    
    branch_id: Mapped[int] = mapped_column(ForeignKey("branches.id"))
    
    users: Mapped[List["MProfile"]] = relationship()