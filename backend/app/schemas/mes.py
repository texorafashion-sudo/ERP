from pydantic import BaseModel


class MachineBase(BaseModel):
    name: str
    code: str
    line: str | None = None
    status: str = "idle"


class Machine(MachineBase):
    id: int

    class Config:
        orm_mode = True
