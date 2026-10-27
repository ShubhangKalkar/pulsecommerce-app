# Week 1: build the PulseCommerce API

Goal: a tested, documented FastAPI service running in Docker, with a real order state machine and correct inventory handling. About 10-15 hours across 7 sessions. One PR per day.

## Database schema

| Table | Key columns |
|---|---|
| `customers` | id, email (unique), name, region, created_at |
| `products` | id, sku (unique), name, price_cents, category |
| `warehouses` | id, name, region |
| `inventory` | product_id, warehouse_id, quantity (composite key) |
| `orders` | id, customer_id, status, total_cents, currency, idempotency_key (unique), created_at |
| `order_items` | id, order_id, product_id, quantity, unit_price_cents |
| `payments` | id, order_id, status, provider, amount_cents, created_at |
| `shipments` | id, order_id, warehouse_id, status, carrier, shipped_at, delivered_at |
| `order_events` | id, order_id, type, payload (JSONB), created_at |

Money is stored as integer cents, never floats. `order_events` is an append-only history that later feeds Kafka (Week 4).

## Order state machine

`placed -> paid -> packed -> shipped -> delivered`, plus `cancelled` and `payment_failed`.

- Transitions are enforced in the service layer, not in routers.
- An invalid transition returns 409 with the standard error body.
- Every transition writes a row to `order_events` in the same transaction.

## Endpoints (Week 1)

- `GET /health`, `GET /ready`
- `GET /v1/products`, `GET /v1/customers`
- `GET /v1/orders` (cursor pagination, filters: status, date range, customer, sort)
- `GET /v1/orders/{id}`
- `POST /v1/orders` (requires `Idempotency-Key`)
- `POST /v1/orders/{id}/pay`, `/ship`, `/cancel`

Error shape: `{ "error": { "code": "...", "message": "...", "request_id": "..." } }`.

## Day by day

**Day 1: Setup and skeleton (done).** FastAPI app with `/health` and `/ready`, JSON logging with request IDs, Docker Compose with Postgres, CI, PR template.

**Day 2: Models and migrations.**
- SQLAlchemy 2.0 models for the tables above, Alembic migrations, and a seed script (50 products, 500 customers, 3 warehouses, inventory rows).
- Done when: `alembic upgrade head` builds the schema and seeding fills it.

**Day 3: Read endpoints.**
- List and detail endpoints with cursor (keyset) pagination on `created_at` and `id`, filtering, sorting, consistent errors.
- Done when: you can page through 10,000 seeded orders with stable results.

**Day 4: Write endpoints and the state machine.**
- `POST /v1/orders` with `Idempotency-Key`: the same key returns the original response, never a duplicate order.
- `pay`, `ship`, `cancel` with transition rules, each writing an `order_events` row, all in transactions.
- Done when: invalid transitions fail with 409 and retrying a POST creates no duplicate.

**Day 5: Inventory correctness.**
- Reserve stock when an order is placed, using `SELECT ... FOR UPDATE` or an atomic conditional update so concurrent orders cannot oversell.
- Concurrency test: 50 parallel orders against 10 units of stock.
- Done when: exactly 10 succeed and the rest get a clean "out of stock" error.

**Day 6: Tests and OpenAPI.**
- Pytest with a test database: unit tests for the state machine, API tests for happy and failure paths.
- OpenAPI descriptions, examples, and tags. Run Schemathesis against the spec.
- Done when: tests pass in one command and Schemathesis runs clean, or its findings are logged and fixed.

**Day 7: Review and write-up.**
- Add indexes for slow queries, with `EXPLAIN ANALYZE` before and after on one query.
- Add DECISIONS.md entries (money as cents, cursor over offset, idempotency approach).
- README that lets a fresh clone run end to end.

## Interview angles for this week
- Why cursor pagination over offset?
- How does idempotency work, and what happens on a concurrent duplicate request?
- How do you prevent overselling under concurrency, and what are the trade-offs between row locks and optimistic checks?
- Why keep the state machine in the service layer?
