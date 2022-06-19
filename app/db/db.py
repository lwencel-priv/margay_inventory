from codecs import ignore_errors

from elasticsearch import AsyncElasticsearch

from app.consts import ELASTIC_AUTH_CONFIG

elastic = AsyncElasticsearch(**ELASTIC_AUTH_CONFIG)


async def initialize() -> None:
    await elastic.ilm.put_lifecycle(
        name="lt-40GB",
        policy={
            "_meta": {
                "description": "40GB per index",
            },
            "phases": {
                "hot": {
                    "min_age": "0ms",
                    "actions": {
                        "rollover": {
                            "max_primary_shard_size": "40gb",
                        },
                    },
                },
            },
        },
    )
    await elastic.indices.put_index_template(
        name="inventory",
        index_patterns=["inventory*"],
        template={
            "settings": {"index": {"number_of_replicas": "1"}},
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "name": {"type": "keyword"},
                    "amount": {"type": "double"},
                    "unit": {"type": "keyword"},
                    "type": {"type": "keyword"},
                },
            },
        },
    )
    if not (await elastic.indices.exists(index="inventory")):
        await elastic.indices.create(
            index="inventory-00001",
            aliases={"inventory": {"is_write_index": True}},
        )


async def close() -> None:
    await elastic.close()
