import uvicorn
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.api import router_v1
from app.consts import (ELASTIC_APM_CONFIG, SERVICE_HOST, SERVICE_NAME,
                        SERVICE_PORT, CORS)
from app.db import db

app = FastAPI(
    title=SERVICE_NAME,
    docs_url="/api/inventory/docs",
    openapi_url="/api/inventory",
)
app.add_middleware(ElasticAPM, client=make_apm_client(ELASTIC_APM_CONFIG))
app.add_middleware(CORSMiddleware, **CORS)


@app.on_event("startup")
async def on_startup() -> None:
    await db.initialize()


@app.on_event("shutdown")
async def app_shutdown() -> None:
    await db.close()


app.include_router(router_v1)

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVICE_HOST, reload=True, port=SERVICE_PORT)
