from datetime import date
from pydantic import BaseModel


class InvoiceBase(BaseModel):
    invoice_no: str
    customer_name: str
    amount: float
    status: str = "unpaid"
    issued_on: date


class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
