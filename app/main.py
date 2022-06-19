import uvicorn
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI

from app.api import router
from app.consts import (ELASTIC_APM_CONFIG, SERVICE_HOST, SERVICE_NAME,
                        SERVICE_PORT)
from app.db import db

app = FastAPI(
    title=SERVICE_NAME,
    docs_url="/api/docs",
    openapi_url="/api",
)
# app.add_middleware(ElasticAPM, make_apm_client(ELASTIC_APM_CONFIG))


@app.on_event("startup")
async def on_startup() -> None:
    await db.initialize()


@app.on_event("shutdown")
async def app_shutdown() -> None:
    await db.close()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVICE_HOST, reload=True, port=SERVICE_PORT)
