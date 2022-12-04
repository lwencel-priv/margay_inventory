from fastapi import APIRouter
from typing import Dict

from app.db.crud import CRUD
from app.db.schemas.item import Item, ItemInDB, ItemAvailability
from . import router_v1

crud = CRUD(
    es_index="inventory",
    create_schema=Item,
    response_schema=ItemInDB,
)


@router_v1.get("/", response_model=list[ItemInDB])
async def get(
    offset: int = 0,
    limit: int = 1,
) -> list[ItemInDB]:
    return await crud.read(
        size=limit,
        query={"match_all": {}}
    )


@router_v1.post("/", response_model=ItemInDB)
async def post(recipe: Item) -> ItemInDB:
    return await crud.create(recipe)

@router_v1.patch("/", response_model=ItemInDB)
async def patch(recipe: ItemInDB) -> ItemInDB:
    return await crud.update(recipe)

@router_v1.delete("/")
async def delete(doc_id: str) -> None:
    await crud.delete(doc_id)


@router_v1.get("/{name}", response_model=list[ItemInDB])
async def get_by_name(
    name: str,
) -> list[ItemInDB]:
    return await crud.read(
        query={
            "match_phrase": {
                "name": name,
            }
        }
    )


@router_v1.delete("/{name}")
async def delete_by_name(
    name: str,
) -> None:
    data: list[ItemInDB] = await crud.read(
        query={
            "match_phrase": {
                "name": name,
            }
        }
    )
    await delete(data[0].id)


@router_v1.post("/check", response_model=list[ItemAvailability])
async def check(items: list[Item]) -> list[ItemAvailability]:
    should_statements = []
    required_items: Dict[str, ItemAvailability] = {}
    for item in items:
        if item.name not in required_items:
            required_items[item.name] = ItemAvailability(
                name=item.name,
                amount=0,
                target_amount=0,
                unit=item.unit,
                available=False,
            )
        
        required_items[item.name].amount += item.amount
        should_statements.append(
            {"term" : { "name" : item.name }}
        )

    query = {
        "bool" : {
            "should" : should_statements,
            "minimum_should_match" : 1
        }
    }
    available_items = await crud.read(query=query)
    for item in available_items:
        required_item = required_items.get(item.name)
        if item.amount >= required_item.amount:
            required_item.available = True


    return list(required_items.values())
