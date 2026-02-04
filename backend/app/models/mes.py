from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    code = Column(String(30), unique=True, nullable=False)
    line = Column(String(120))
    status = Column(String(30), default="idle")


class ProductionLog(Base):
    __tablename__ = "production_logs"

    id = Column(Integer, primary_key=True)
    work_order_id = Column(Integer, ForeignKey("work_orders.id"), nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    operator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(30), nullable=False)
    good_qty = Column(Numeric(12, 2), default=0)
    reject_qty = Column(Numeric(12, 2), default=0)
    downtime_reason = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())

    machine = relationship("Machine")
