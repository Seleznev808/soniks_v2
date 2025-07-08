from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.core.config import PostgresSettings, Settings, SQLEngineSettings
from src.core.container import get_providers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    await app.state.dishka_container.close()


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        debug=settings.app.DEBUG,
    )

    context = {
        PostgresSettings: settings.postgres,
        SQLEngineSettings: settings.sql_engine,
    }

    container = make_async_container(*get_providers(), context=context)
    setup_dishka(container, app)

    return app
