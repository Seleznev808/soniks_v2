from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.transaction import Transaction


class TransactionORM(Transaction):
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
