from fastapi import APIRouter

from app.db.crud import CRUD
from app.db.schemas.item import Item, ItemInDB

recipe_router = APIRouter(prefix="/inventory")
crud = CRUD(
    es_index="inventory",
    create_schema=Item,
    response_schema=ItemInDB,
)


@recipe_router.get("/", response_model=list[ItemInDB])
async def get(
    offset: int = 0,
    limit: int = 1,
) -> list[ItemInDB]:
    return await crud.read(query={"match_all": {}})


@recipe_router.post("/", response_model=ItemInDB)
async def post(recipe: Item) -> ItemInDB:
    return await crud.create(recipe)


@recipe_router.delete("/")
async def delete(doc_id: str) -> None:
    await crud.delete(doc_id)


@recipe_router.get("/{name}", response_model=list[ItemInDB])
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


@recipe_router.delete("/{name}")
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
