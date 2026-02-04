# Scalability Notes

- **Stateless APIs:** FastAPI services can scale horizontally behind a load balancer.
- **Database:** Use PostgreSQL with partitioning for high-volume production logs.
- **Caching:** Add Redis for hot data such as dashboards and lookup tables.
- **Async Processing:** Use Celery/RQ for heavy jobs (MRP runs, batch costing, reports).
- **Observability:** Centralize logs with OpenTelemetry and metrics dashboards.
- **Security:** Rotate JWT secrets, enforce MFA for Admin and Finance roles.
