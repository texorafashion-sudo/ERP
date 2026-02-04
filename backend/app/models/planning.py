from sqlalchemy import Column, Date, Integer, Numeric, String

from app.models.base import Base


class MasterProductionSchedule(Base):
    __tablename__ = "mps"

    id = Column(Integer, primary_key=True)
    item_code = Column(String(50), nullable=False)
    planned_date = Column(Date, nullable=False)
    planned_qty = Column(Numeric(12, 2), nullable=False)
    priority = Column(Integer, default=3)


class CapacityPlan(Base):
    __tablename__ = "capacity_plans"

    id = Column(Integer, primary_key=True)
    work_center = Column(String(120), nullable=False)
    available_hours = Column(Numeric(12, 2), nullable=False)
    required_hours = Column(Numeric(12, 2), nullable=False)
    plan_date = Column(Date, nullable=False)
