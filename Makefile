COMPOSE_FILE = docker_compose/local.yml
APP_SERVICE = soniks-backend

.PHONY: format, up_local, up_build_local, stop_local, makemigrations, migrate, downgrade

format:
	uv run ruff format
	uv run ruff check --fix

up_local:
	docker compose -f $(COMPOSE_FILE) up -d

up_build_local:
	docker compose -f $(COMPOSE_FILE) up -d --build

stop_local:
	docker compose -f $(COMPOSE_FILE) stop

makemigrations:
	POSTGRES__HOST=localhost PYTHONPATH=src alembic revision --autogenerate -m="$(m)"

migrate:
	docker exec -it $(APP_SERVICE) sh -c "PYTHONPATH=src alembic upgrade head"

downgrade:
	docker exec -it $(APP_SERVICE) sh -c "PYTHONPATH=src alembic downgrade -1"
