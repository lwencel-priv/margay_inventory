import uuid
from typing import Type

from app.db.db import elastic
from app.db.schemas import CreateSchemaType, ResponseSchemaType


class CRUD:
    def __init__(
        self, es_index: str, create_schema: Type[CreateSchemaType], response_schema: Type[ResponseSchemaType]
    ) -> None:
        self._es_index = es_index
        self._create_schema = create_schema
        self._response_schema = response_schema

    async def create(self, recipe: CreateSchemaType) -> ResponseSchemaType:
        doc_id = uuid.uuid4().hex
        doc = recipe.dict()
        await elastic.create(
            index=self._es_index,
            id=doc_id,
            document=doc,
        )
        doc["id"] = doc_id
        return self._response_schema(**doc)

    async def read(self, query: dict) -> list[ResponseSchemaType]:
        response = await elastic.search(
            index=self._es_index,
            query=query,
        )
        items = []
        for item in response.get("hits", {}).get("hits", []):
            items.append(
                self._response_schema(
                    id=item["_id"],
                    **item["_source"],
                )
            )

        return items

    async def update(self) -> None:
        pass

    async def delete(self, doc_id: str) -> None:
        await elastic.delete(
            index=self._es_index,
            id=doc_id,
        )
