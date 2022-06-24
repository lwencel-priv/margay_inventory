from pydantic import BaseModel


class Item(BaseModel):
    name: str
    amount: int
    unit: str


class ItemInDB(Item):
    id: str


class ItemAvailability(Item):
    available: bool