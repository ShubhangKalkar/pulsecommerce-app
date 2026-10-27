# Decisions log

Each entry: the decision, the alternatives I considered, and why.

## 001: Trunk-based development with short-lived branches
- **Decision:** `main` stays deployable; every change goes through a PR from a branch like `feat/...` or `fix/...`; squash merge.
- **Alternatives:** GitFlow (long-lived `develop` and release branches).
- **Why:** Smaller diffs, faster feedback, and it matches how GitOps and preview environments work.

## 002: Layered structure (routers, services, repositories)
- **Decision:** Routers handle HTTP, services hold business rules, repositories hold queries.
- **Why:** The order state machine and inventory rules can be tested without HTTP or a real database.

## 003: Structured JSON logs with a request ID
- **Decision:** Every log line is JSON and carries the request ID from the `X-Request-ID` header, or a generated one.
- **Why:** Lets me trace one request across logs later in Grafana and Loki.
