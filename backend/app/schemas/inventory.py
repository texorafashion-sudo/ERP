from pydantic import BaseModel


class InventoryItemBase(BaseModel):
    item_code: str
    description: str | None = None
    category: str | None = None
    uom: str


class InventoryItem(InventoryItemBase):
    id: int

    class Config:
        orm_mode = True
