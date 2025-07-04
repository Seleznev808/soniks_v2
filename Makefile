COMPOSE_FILE = docker_compose/local.yml
APP_SERVICE = soniks-backend

.PHONY: format, up, up_build, stop, down, down_v, bash, logs

format:
	uv run ruff format
	uv run ruff check --fix

up:
	docker compose -f $(COMPOSE_FILE) up -d

up_build:
	docker compose -f $(COMPOSE_FILE) up -d --build

stop:
	docker compose -f $(COMPOSE_FILE) stop

down:
	docker compose -f $(COMPOSE_FILE) down

down_v:
	docker compose -f $(COMPOSE_FILE) down -v

bash:
	docker exec -it $(APP_SERVICE) bash

logs:
	docker logs $(APP_SERVICE)


.PHONY: makemigrations, migrate, downgrade

makemigrations:
	POSTGRES__HOST=localhost PYTHONPATH=src alembic revision --autogenerate -m="$(m)"

migrate:
	docker exec -it $(APP_SERVICE) sh -c "PYTHONPATH=src alembic upgrade head"

downgrade:
	docker exec -it $(APP_SERVICE) sh -c "PYTHONPATH=src alembic downgrade -1"
