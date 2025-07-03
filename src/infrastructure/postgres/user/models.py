from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.postgres.base import BaseORM
from infrastructure.postgres.mixins import TimestampMixin, UUIDMixin


class UserORM(BaseORM, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
