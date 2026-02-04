from sqlalchemy import Column, Date, Integer, Numeric, String

from app.models.base import Base


class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(Integer, primary_key=True)
    order_no = Column(String(50), unique=True, nullable=False)
    customer_name = Column(String(120), nullable=False)
    order_date = Column(Date, nullable=False)
    status = Column(String(30), default="open")
    total_amount = Column(Numeric(12, 2), nullable=False)
