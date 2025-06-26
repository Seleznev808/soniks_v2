FROM python:3.12.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.7.15 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG WORKDIR=/app

ENV PATH="$WORKDIR/.venv/bin/:${PATH}"

WORKDIR $WORKDIR

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY pyproject.toml uv.lock ./

COPY src/ .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
