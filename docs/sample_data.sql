INSERT INTO roles (name, description) VALUES
('Admin', 'System administrator'),
('Production Manager', 'Production planning and control'),
('Shop Floor Operator', 'Runs machines and logs output'),
('Quality Inspector', 'Inspects and approves quality'),
('Store / Inventory Manager', 'Inventory operations'),
('Accounts / Finance', 'Finance control'),
('Sales', 'Customer orders and delivery'),
('HR', 'Employee records');

INSERT INTO customers (name, contact_name, phone) VALUES
('Atlas Motors', 'Diego R.', '+1-555-0100'),
('Northwind Components', 'Rita L.', '+1-555-0101');

INSERT INTO suppliers (name, contact_name) VALUES
('SteelWorks', 'Marta K.'),
('Precision Plastics', 'Hugo V.');

INSERT INTO warehouses (name, code, location) VALUES
('Main Warehouse', 'WH-MAIN', 'Plant 1');

INSERT INTO inventory_items (item_code, description, category, uom) VALUES
('RM-STEEL-01', 'Steel Sheet', 'Raw', 'KG'),
('FG-MOTOR-01', 'Electric Motor', 'Finished', 'EA');
