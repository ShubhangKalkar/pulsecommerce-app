# PulseCommerce

Order and fulfillment platform. Week 1 builds the API: FastAPI, PostgreSQL, Docker.

## Run it
```bash
make up
```
Then open http://localhost:8000/docs.

## Develop
```bash
cd api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
make test     # from the repo root
make lint
```

## Workflow
Branch from `main` (`feat/...`, `fix/...`, `chore/...`), open a PR, wait for the `test` and `docker-build` checks, squash merge.
