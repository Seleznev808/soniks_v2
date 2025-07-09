from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.uow import UnitOfWork


class UnitOfWorkORM(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self) -> None:
        await self.rollback()
