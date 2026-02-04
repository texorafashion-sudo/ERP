# FactorySphere ERP

FactorySphere is a modular Manufacturing ERP suite combining MES, QMS, Production Planning, Inventory, Accounting, and HR for mid-sized factories (50–500 employees). It is designed for fast shop-floor operations, clear dashboards, and role-based access control.

## Modules
- Manufacturing ERP (customer, supplier, BOM, routing, costing, WIP tracking)
- Production Planning & Scheduling (MPS, capacity planning, Gantt)
- MES (real-time tracking, operator login, OEE, downtime)
- Inventory Management (multi-warehouse, FIFO/LIFO, valuation)
- QMS (inspections, NC, CAPA, audit history)
- Accounting & Finance (COA, invoices, P&L)
- HR & Payroll (employee master, attendance, payroll basics)

## Repo Structure
```
backend/     FastAPI services, schemas, data models
frontend/    Responsive UI (dashboard + navigation)
docs/        Database schema, API guide, installation, scalability notes
```

## Quick Start
- Backend: `docs/installation.md`
- Frontend: `docs/installation.md`
- Database schema: `docs/database_schema.sql`
- Testing guide: `docs/testing.md`

## Notes
- Use `docs/sample_data.sql` to populate demo roles, customers, and inventory.
- Update secrets and connection strings in `backend/app/core/config.py`.
