from typing import TYPE_CHECKING, List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, relationship

from core.api.v1.models.base import OrmBase


if TYPE_CHECKING:
    from .workspace import MWorkspace


class MBranch(OrmBase):
    __tablename__ = "branches"
    
    name: Mapped[str]
    
    inn: Mapped[BigInteger]
    kpp: Mapped[BigInteger]
    ogrn: Mapped[BigInteger]
    
    rc_bic: Mapped[BigInteger]
    acc: Mapped[BigInteger]
    corr_acc: Mapped[BigInteger]
    
    workspaces: Mapped[List["MWorkspace"]] = relationship()
    