from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID


class UserRole(StrEnum):
    # ToDO: роли для примера
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    USER = "user"


@dataclass(kw_only=True)
class User:
    uuid: UUID
    username: str
    email: str
    role: UserRole
    is_active: bool

    @classmethod
    def create(
        cls,
        uuid: UUID,
        username: str,
        email: str,
    ) -> "User":
        cls(
            uuid=uuid,
            username=username,
            email=email,
            role=UserRole.USER,
            is_active=True,
        )
