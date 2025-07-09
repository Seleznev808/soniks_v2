from typing import Protocol
from uuid import UUID

from src.domain.entities.user import User


class UserRepository(Protocol):
    async def get_user_by_id(self, user_id: UUID) -> User | None: ...

    async def create_user(self, user: User) -> User: ...
