from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.user import User, UserRole
from src.infrastructure.postgres.models.base import BaseORM
from src.infrastructure.postgres.models.mixins import TimestampMixin, UUIDMixin


class UserORM(BaseORM, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(128), unique=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        default=UserRole.USER,
    )
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)

    def to_entity(self) -> User:
        return User(
            uuid=self.uuid,
            username=self.username,
            email=self.email,
            role=self.role,
            is_active=self.is_active,
        )

    @classmethod
    def from_entity(cls, entity: User) -> "UserORM":
        return cls(
            uuid=entity.uuid,
            username=entity.username,
            email=entity.email,
            role=entity.role,
            is_active=entity.is_active,
        )
