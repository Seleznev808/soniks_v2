COMPOSE_FILE = docker_compose/local.yml

.PHONY: format, up_local, up_build_local, stop_local

format:
	uv run ruff format
	uv run ruff check --fix

up_local:
	docker compose -f $(COMPOSE_FILE) up -d

up_build_local:
	docker compose -f $(COMPOSE_FILE) up -d --build

stop_local:
	docker compose -f $(COMPOSE_FILE) stop
