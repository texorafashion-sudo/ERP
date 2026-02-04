# API Structure

Base URL: `/api/v1`

## Manufacturing
- `GET /manufacturing/overview` – KPIs for work orders, BOMs, sales orders.

## Planning
- `GET /planning/schedule` – Gantt placeholders, bottleneck alerts.

## MES
- `GET /mes/live` – Live production stats and OEE.

## Inventory
- `GET /inventory/summary` – Stock summary by category.

## Quality
- `GET /quality/metrics` – Inspection pass rates and defects.

## Accounting
- `GET /accounting/finance` – Financial KPIs snapshot.

## Sales
- `GET /sales/pipeline` – Sales pipeline metrics.

## Auth
Planned endpoints:
- `POST /auth/login`
- `POST /auth/refresh`
- `GET /auth/me`
