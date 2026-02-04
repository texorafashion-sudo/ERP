-- FactorySphere ERP master schema
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    role_id INTEGER NOT NULL REFERENCES roles(id),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    contact_name VARCHAR(120),
    phone VARCHAR(50),
    email VARCHAR(120),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    contact_name VARCHAR(120),
    phone VARCHAR(50),
    email VARCHAR(120),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE boms (
    id SERIAL PRIMARY KEY,
    item_code VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    revision VARCHAR(30),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE bom_components (
    id SERIAL PRIMARY KEY,
    bom_id INTEGER NOT NULL REFERENCES boms(id),
    component_code VARCHAR(50) NOT NULL,
    quantity NUMERIC(12,4) NOT NULL,
    uom VARCHAR(20) NOT NULL
);

CREATE TABLE routings (
    id SERIAL PRIMARY KEY,
    item_code VARCHAR(50) NOT NULL,
    operation_name VARCHAR(120) NOT NULL,
    work_center VARCHAR(120) NOT NULL,
    standard_minutes INTEGER NOT NULL
);

CREATE TABLE work_orders (
    id SERIAL PRIMARY KEY,
    work_order_no VARCHAR(50) UNIQUE NOT NULL,
    item_code VARCHAR(50) NOT NULL,
    quantity NUMERIC(12,2) NOT NULL,
    planned_start DATE,
    planned_end DATE,
    status VARCHAR(30) DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    code VARCHAR(30) UNIQUE NOT NULL,
    location VARCHAR(255)
);

CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    item_code VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255),
    category VARCHAR(50),
    uom VARCHAR(20) NOT NULL
);

CREATE TABLE stock_ledger (
    id SERIAL PRIMARY KEY,
    item_id INTEGER NOT NULL REFERENCES inventory_items(id),
    warehouse_id INTEGER NOT NULL REFERENCES warehouses(id),
    quantity NUMERIC(12,2) NOT NULL,
    transaction_type VARCHAR(30) NOT NULL,
    reference VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE machines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    code VARCHAR(30) UNIQUE NOT NULL,
    line VARCHAR(120),
    status VARCHAR(30) DEFAULT 'idle'
);

CREATE TABLE production_logs (
    id SERIAL PRIMARY KEY,
    work_order_id INTEGER NOT NULL REFERENCES work_orders(id),
    machine_id INTEGER NOT NULL REFERENCES machines(id),
    operator_id INTEGER NOT NULL REFERENCES users(id),
    status VARCHAR(30) NOT NULL,
    good_qty NUMERIC(12,2) DEFAULT 0,
    reject_qty NUMERIC(12,2) DEFAULT 0,
    downtime_reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE mps (
    id SERIAL PRIMARY KEY,
    item_code VARCHAR(50) NOT NULL,
    planned_date DATE NOT NULL,
    planned_qty NUMERIC(12,2) NOT NULL,
    priority INTEGER DEFAULT 3
);

CREATE TABLE capacity_plans (
    id SERIAL PRIMARY KEY,
    work_center VARCHAR(120) NOT NULL,
    available_hours NUMERIC(12,2) NOT NULL,
    required_hours NUMERIC(12,2) NOT NULL,
    plan_date DATE NOT NULL
);

CREATE TABLE inspections (
    id SERIAL PRIMARY KEY,
    inspection_type VARCHAR(30) NOT NULL,
    reference VARCHAR(50) NOT NULL,
    inspector_id INTEGER NOT NULL REFERENCES users(id),
    status VARCHAR(30) DEFAULT 'pending',
    inspected_on DATE NOT NULL
);

CREATE TABLE non_conformances (
    id SERIAL PRIMARY KEY,
    reference VARCHAR(50) NOT NULL,
    category VARCHAR(120) NOT NULL,
    description VARCHAR(255),
    status VARCHAR(30) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE capa (
    id SERIAL PRIMARY KEY,
    nc_id INTEGER NOT NULL REFERENCES non_conformances(id),
    action VARCHAR(255) NOT NULL,
    owner VARCHAR(120),
    due_date DATE,
    status VARCHAR(30) DEFAULT 'open'
);

CREATE TABLE chart_of_accounts (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(120) NOT NULL,
    account_type VARCHAR(50) NOT NULL
);

CREATE TABLE journal_entries (
    id SERIAL PRIMARY KEY,
    entry_date DATE NOT NULL,
    description VARCHAR(255),
    debit NUMERIC(12,2) DEFAULT 0,
    credit NUMERIC(12,2) DEFAULT 0,
    account_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_no VARCHAR(50) UNIQUE NOT NULL,
    customer_name VARCHAR(120) NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    status VARCHAR(30) DEFAULT 'unpaid',
    issued_on DATE NOT NULL
);

CREATE TABLE sales_orders (
    id SERIAL PRIMARY KEY,
    order_no VARCHAR(50) UNIQUE NOT NULL,
    customer_name VARCHAR(120) NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'open',
    total_amount NUMERIC(12,2) NOT NULL
);
