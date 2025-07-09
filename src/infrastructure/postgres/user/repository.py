from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.user.repository import UserRepository
from src.domain.entities.user import User
from src.infrastructure.postgres.user.models import UserORM


class UserRepositoryORM(UserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        stmt = select(UserORM).where(UserORM.uuid == user_id)
        result = await self._session.execute(stmt)
        user_orm = result.scalar_one_or_none()

        if not user_orm:
            return None

        return user_orm.to_entity()

    async def create_user(self, user: User) -> User:
        user_orm = UserORM.from_entity(user)
        self._session.add(user_orm)

        return user_orm.to_entity()
