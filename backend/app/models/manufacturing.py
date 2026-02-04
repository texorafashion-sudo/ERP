from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    contact_name = Column(String(120))
    phone = Column(String(50))
    email = Column(String(120))
    address = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    contact_name = Column(String(120))
    phone = Column(String(50))
    email = Column(String(120))
    address = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())


class BillOfMaterial(Base):
    __tablename__ = "boms"

    id = Column(Integer, primary_key=True)
    item_code = Column(String(50), nullable=False)
    description = Column(String(255))
    revision = Column(String(30))
    created_at = Column(DateTime, server_default=func.now())

    components = relationship("BOMComponent", back_populates="bom", cascade="all, delete")


class BOMComponent(Base):
    __tablename__ = "bom_components"

    id = Column(Integer, primary_key=True)
    bom_id = Column(Integer, ForeignKey("boms.id"), nullable=False)
    component_code = Column(String(50), nullable=False)
    quantity = Column(Numeric(12, 4), nullable=False)
    uom = Column(String(20), nullable=False)

    bom = relationship("BillOfMaterial", back_populates="components")


class Routing(Base):
    __tablename__ = "routings"

    id = Column(Integer, primary_key=True)
    item_code = Column(String(50), nullable=False)
    operation_name = Column(String(120), nullable=False)
    work_center = Column(String(120), nullable=False)
    standard_minutes = Column(Integer, nullable=False)


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True)
    work_order_no = Column(String(50), unique=True, nullable=False)
    item_code = Column(String(50), nullable=False)
    quantity = Column(Numeric(12, 2), nullable=False)
    planned_start = Column(Date)
    planned_end = Column(Date)
    status = Column(String(30), default="planned")
    created_at = Column(DateTime, server_default=func.now())
