FROM python:3.12.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.7.15 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV UV_PROJECT_ENVIRONMENT=/usr/local

ARG WORKDIR=/app

WORKDIR $WORKDIR

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY pyproject.toml uv.lock alembic.ini ./

COPY src/ ./src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
