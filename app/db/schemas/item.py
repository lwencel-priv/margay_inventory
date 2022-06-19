from pydantic import BaseModel


class Item(BaseModel):
    name: str
    amount: int
    unit: str
    type: str


class ItemInDB(Item):
    id: str
