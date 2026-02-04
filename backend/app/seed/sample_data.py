from datetime import date

from sqlalchemy.orm import Session

from app.models.accounting import ChartOfAccount, Invoice
from app.models.core import Role, User
from app.models.inventory import InventoryItem, Warehouse
from app.models.manufacturing import Customer, Supplier, WorkOrder
from app.models.mes import Machine
from app.models.planning import MasterProductionSchedule
from app.models.quality import Inspection
from app.models.sales import SalesOrder


def seed_data(db: Session) -> None:
    roles = [
        Role(name="Admin", description="System administrator"),
        Role(name="Production Manager", description="Production planning and control"),
        Role(name="Shop Floor Operator", description="Runs machines and logs output"),
        Role(name="Quality Inspector", description="Inspects and approves quality"),
    ]
    db.add_all(roles)
    db.flush()

    admin = User(
        full_name="Priya Nair",
        email="admin@factorysphere.local",
        hashed_password="CHANGE_ME",
        role_id=roles[0].id,
    )
    db.add(admin)

    customers = [
        Customer(name="Atlas Motors", contact_name="Diego R.", phone="+1-555-0100"),
        Customer(name="Northwind Components", contact_name="Rita L.", phone="+1-555-0101"),
    ]
    suppliers = [
        Supplier(name="SteelWorks", contact_name="Marta K."),
        Supplier(name="Precision Plastics", contact_name="Hugo V."),
    ]
    db.add_all(customers + suppliers)

    warehouse = Warehouse(name="Main Warehouse", code="WH-MAIN", location="Plant 1")
    db.add(warehouse)

    items = [
        InventoryItem(item_code="RM-STEEL-01", description="Steel Sheet", category="Raw", uom="KG"),
        InventoryItem(item_code="FG-MOTOR-01", description="Electric Motor", category="Finished", uom="EA"),
    ]
    db.add_all(items)

    work_order = WorkOrder(
        work_order_no="WO-10045",
        item_code="FG-MOTOR-01",
        quantity=250,
        planned_start=date.today(),
        planned_end=date.today(),
        status="released",
    )
    db.add(work_order)

    machine = Machine(name="Press 02", code="PR-02", line="Pressing", status="running")
    db.add(machine)

    mps = MasterProductionSchedule(
        item_code="FG-MOTOR-01",
        planned_date=date.today(),
        planned_qty=300,
        priority=1,
    )
    db.add(mps)

    inspection = Inspection(
        inspection_type="final",
        reference="WO-10045",
        inspector_id=1,
        status="passed",
        inspected_on=date.today(),
    )
    db.add(inspection)

    account = ChartOfAccount(code="4000", name="Sales Revenue", account_type="Income")
    invoice = Invoice(
        invoice_no="INV-9001",
        customer_name="Atlas Motors",
        amount=52000,
        status="unpaid",
        issued_on=date.today(),
    )
    db.add(account)
    db.add(invoice)

    sales_order = SalesOrder(
        order_no="SO-7001",
        customer_name="Northwind Components",
        order_date=date.today(),
        status="open",
        total_amount=87000,
    )
    db.add(sales_order)

    db.commit()
