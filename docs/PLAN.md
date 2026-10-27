# 8-week plan

Check items off as they merge. Each phase ends with something demoable.

## Week 1: API foundation
- [x] Day 1: repo, Docker Compose, CI, PR template (branch protection is a manual GitHub setting)
- [ ] Day 2: SQLAlchemy models, Alembic migrations, seed script (50 products, 500 customers, 3 warehouses)
- [ ] Day 3: read endpoints (products, customers, orders), cursor pagination, filters, error format
- [ ] Day 4: POST orders with Idempotency-Key, pay/ship/cancel, order state machine, order_events
- [ ] Day 5: inventory reservation without overselling (row locking), concurrency test (50 parallel orders vs 10 units)
- [ ] Day 6: pytest suite, OpenAPI polish, Schemathesis run
- [ ] Day 7: EXPLAIN ANALYZE + index, DECISIONS.md, README

Details for each day are in `docs/WEEK1.md`.

## Week 2: production-grade API
- [ ] JWT auth and API keys, rate limiting, CORS
- [ ] Redis caching with before/after latency numbers
- [ ] Webhook subscriptions, k6 load test
- [ ] React dashboard (overview, orders table) with Vercel/Netlify PR previews

## Week 3: Kubernetes and GitOps
- [ ] kind cluster, `pulsecommerce-config` repo (Kustomize), ArgoCD
- [ ] CI builds image, pushes to GHCR, updates image tag in config repo
- [ ] ingress-nginx, HPA, k6-triggered autoscaling demo
- [ ] ArgoCD ApplicationSet per-PR preview environments with cleanup

## Weeks 4-5: streaming and lake
- [ ] Simulator -> Redpanda; Spark Structured Streaming -> MinIO (bronze, silver)
- [ ] Gold aggregates into Postgres; API serves real data; SSE live updates
- [ ] Deploy pipeline pieces as ArgoCD apps

## Weeks 6-7: orchestration, AWS-style services, warehouse
- [ ] Airflow DAGs, dbt models, Great Expectations checks
- [ ] LocalStack: Lambda consumer, DynamoDB, SQS/SNS, S3, IAM
- [ ] Publish gold tables to Databricks; API queries it through a SQL endpoint
- [ ] Argo Rollouts canary with automatic rollback
- [ ] Optional: serverless variant of 2-3 endpoints

## Week 8: polish
- [ ] Prometheus + Grafana, Terraform, README with architecture diagram
- [ ] 3-5 minute demo video, practice explaining every decision in DECISIONS.md
