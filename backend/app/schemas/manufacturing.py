from datetime import date
from pydantic import BaseModel


class WorkOrderBase(BaseModel):
    work_order_no: str
    item_code: str
    quantity: float
    planned_start: date | None = None
    planned_end: date | None = None
    status: str = "planned"


class WorkOrder(WorkOrderBase):
    id: int

    class Config:
        orm_mode = True
