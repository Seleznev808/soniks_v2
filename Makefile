.PHONY: format, up, up-build, stop

format:
	uv run ruff format
	uv run ruff check --fix

up:
	docker compose up -d

up-build:
	docker compose up -d --build

stop:
	docker compose stop
