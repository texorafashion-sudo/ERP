from datetime import date
from pydantic import BaseModel


class SalesOrderBase(BaseModel):
    order_no: str
    customer_name: str
    order_date: date
    status: str = "open"
    total_amount: float


class SalesOrder(SalesOrderBase):
    id: int

    class Config:
        orm_mode = True
