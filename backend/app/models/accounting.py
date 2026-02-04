from sqlalchemy import Column, Date, DateTime, Integer, Numeric, String
from sqlalchemy.sql import func

from app.models.base import Base


class ChartOfAccount(Base):
    __tablename__ = "chart_of_accounts"

    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(120), nullable=False)
    account_type = Column(String(50), nullable=False)


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True)
    entry_date = Column(Date, nullable=False)
    description = Column(String(255))
    debit = Column(Numeric(12, 2), default=0)
    credit = Column(Numeric(12, 2), default=0)
    account_code = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    invoice_no = Column(String(50), unique=True, nullable=False)
    customer_name = Column(String(120), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    status = Column(String(30), default="unpaid")
    issued_on = Column(Date, nullable=False)
