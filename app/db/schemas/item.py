from pydantic import BaseModel


class BaseItem(BaseModel):
    name: str


class Item(BaseItem):
    amount: float
    unit: str
    target_amount: float


class ItemInDB(Item):
    id: str


class ItemAvailability(Item):
    available: bool
