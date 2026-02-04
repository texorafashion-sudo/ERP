from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(Integer, primary_key=True)
    inspection_type = Column(String(30), nullable=False)
    reference = Column(String(50), nullable=False)
    inspector_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(30), default="pending")
    inspected_on = Column(Date, nullable=False)

    inspector = relationship("app.models.core.User")


class NonConformance(Base):
    __tablename__ = "non_conformances"

    id = Column(Integer, primary_key=True)
    reference = Column(String(50), nullable=False)
    category = Column(String(120), nullable=False)
    description = Column(String(255))
    status = Column(String(30), default="open")
    created_at = Column(DateTime, server_default=func.now())


class CAPA(Base):
    __tablename__ = "capa"

    id = Column(Integer, primary_key=True)
    nc_id = Column(Integer, ForeignKey("non_conformances.id"), nullable=False)
    action = Column(String(255), nullable=False)
    owner = Column(String(120))
    due_date = Column(Date)
    status = Column(String(30), default="open")

    nc = relationship("NonConformance")
