.PHONY: up down logs test lint fmt

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f api

test:
	cd api && pytest -q

lint:
	cd api && ruff check . && ruff format --check .

fmt:
	cd api && ruff check --fix . && ruff format .
