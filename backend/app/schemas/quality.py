from datetime import date
from pydantic import BaseModel


class InspectionBase(BaseModel):
    inspection_type: str
    reference: str
    inspector_id: int
    status: str = "pending"
    inspected_on: date


class Inspection(InspectionBase):
    id: int

    class Config:
        orm_mode = True
