from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    code = Column(String(30), unique=True, nullable=False)
    location = Column(String(255))


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True)
    item_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    category = Column(String(50))
    uom = Column(String(20), nullable=False)


class StockLedger(Base):
    __tablename__ = "stock_ledger"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("inventory_items.id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    quantity = Column(Numeric(12, 2), nullable=False)
    transaction_type = Column(String(30), nullable=False)
    reference = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())

    item = relationship("InventoryItem")
    warehouse = relationship("Warehouse")
