from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from core.config import settings


class BaseORM(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.postgres.NAMING_CONVENTION)
