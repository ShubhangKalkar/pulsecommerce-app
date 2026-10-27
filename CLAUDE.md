# PulseCommerce

Order and fulfillment platform, built as a hands-on portfolio project for backend and data engineering interviews. APIs are the main focus. Everything must stay free (local Docker/Kubernetes, LocalStack, free tiers).

## Stack
- API: FastAPI, SQLAlchemy 2.0, Alembic, PostgreSQL, Redis (from Week 2)
- Later: Redpanda/Kafka, Spark, Airflow, dbt, MinIO/LocalStack (AWS), Kubernetes (kind), ArgoCD, Databricks
- Tests: pytest, Schemathesis, k6, Playwright
- CI: GitHub Actions

## Layout
- `api/app/routers`: HTTP only. `services`: business rules. `repositories`: DB queries. `schemas`: Pydantic models.
- `simulator/`: event generator (used from Week 4)
- `docs/PLAN.md`: the 8-week plan and current progress
- `docs/WEEK1.md`: detailed Week 1 design (schema, state machine, endpoints, daily tasks)
- `DECISIONS.md`: log of design decisions (decision, alternatives, why)

## Commands
- Run: `docker compose up --build` (API at http://localhost:8000/docs)
- Test: `cd api && pytest -q`
- Lint: `cd api && ruff check . && ruff format --check .`

## Workflow rules
- Never commit to `main`. One branch per task: `feat/...`, `fix/...`, `chore/...`, `test/...`.
- Conventional Commits. Open a PR using `.github/pull_request_template.md`. Squash merge.
- CI jobs `test` and `docker-build` must pass.
- Add an entry to `DECISIONS.md` for every non-trivial design choice.

## Code conventions
- Money is stored as integer cents, never floats.
- Order status changes only go through the state machine in `services/`; invalid transitions return 409.
- Every write to an order also appends a row to `order_events`.
- Writes that create resources accept an `Idempotency-Key` header.
- Errors use one consistent JSON shape with a request ID.

## Learning mode
This project exists so the owner can explain every part in an interview.
- Work on one task from `docs/PLAN.md` at a time and stop for review.
- For core logic (order state machine, idempotency, inventory locking, pagination, auth), explain the approach first and let the owner write or review it. Boilerplate (Dockerfiles, CI YAML, manifests, repetitive tests) can be written directly.
- After generating anything non-trivial, explain why it works.
- Call out trade-offs and note them for `DECISIONS.md`.
