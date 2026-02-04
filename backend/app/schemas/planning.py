from datetime import date
from pydantic import BaseModel


class MasterProductionScheduleBase(BaseModel):
    item_code: str
    planned_date: date
    planned_qty: float
    priority: int = 3


class MasterProductionSchedule(MasterProductionScheduleBase):
    id: int

    class Config:
        orm_mode = True
