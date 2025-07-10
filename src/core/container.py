from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.application.interfaces.transaction import Transaction
from src.application.interfaces.user import UserRepository
from src.core.config import PostgresSettings, SQLEngineSettings
from src.infrastructure.postgres.database import (
    get_engine,
    get_session,
    get_sessionmaker,
)
from src.infrastructure.postgres.repositories.user import UserRepositoryORM
from src.infrastructure.postgres.transaction import TransactionORM


def config_provider() -> Provider:
    provider = Provider()

    provider.from_context(provides=PostgresSettings, scope=Scope.APP)
    provider.from_context(provides=SQLEngineSettings, scope=Scope.APP)

    return provider


def db_provider() -> Provider:
    provider = Provider()

    provider.provide(
        get_engine,
        provides=AsyncEngine,
        scope=Scope.APP,
    )
    provider.provide(
        get_sessionmaker,
        provides=async_sessionmaker[AsyncSession],
        scope=Scope.APP,
    )
    provider.provide(
        get_session,
        provides=AsyncSession,
        scope=Scope.REQUEST,
    )

    return provider


def gateway_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)

    provider.provide(TransactionORM, provides=Transaction)
    provider.provide(UserRepositoryORM, provides=UserRepository)

    return provider


def get_providers() -> tuple[Provider, ...]:
    return (
        config_provider(),
        db_provider(),
        gateway_provider(),
    )
