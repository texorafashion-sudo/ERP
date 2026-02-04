# FactorySphere ERP Architecture

## Overview
FactorySphere is designed as a modular ERP suite that unifies Manufacturing ERP, MES, QMS, Planning, Inventory, Finance, and HR. The system is built around a service-oriented backend and a responsive front-end optimized for factory users.

## Core Layers
- **Presentation Layer:** Responsive UI with role-aware navigation, dashboards, and live status indicators.
- **API Layer:** REST APIs grouped by domain modules and secured by JWT.
- **Domain Services:** Orchestrate workflows (production release, inspection, inventory movements).
- **Data Layer:** PostgreSQL schema with transactional safety and audit-ready records.

## Module Map
- **Manufacturing ERP:** BOM, routing, work orders, costing, supplier and customer management.
- **Planning & Scheduling:** MPS, capacity planning, bottleneck alerts, Gantt preparation.
- **MES:** Operator login, machine status, OEE, live production logs.
- **Inventory:** Multi-warehouse stock, bin control, FIFO/LIFO valuation.
- **QMS:** Inspections, non-conformance, CAPA workflows.
- **Accounting:** Chart of accounts, invoices, journal entries.
- **HR:** Employee master, attendance, payroll basics (extensible).

## Security & RBAC
- JWT authentication with role-based access mapping (see `backend/app/services/authorization.py`).
- Modular scopes so each role sees only relevant menus and data.

## Integration Strategy
- Event-driven hooks for manufacturing events to update inventory, finance, and quality.
- API-first design supports integration with barcode scanners, IIoT sensors, and BI tools.
