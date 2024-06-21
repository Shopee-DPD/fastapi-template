import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import Base, engine
from app.middleware.router_logging import RouterLoggingMiddleware
from app.middleware.sql import SQLAlchemyMiddleware
from app.settings.config import AppSettings
from app.settings.logging import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)  # type: ignore

app_settings = AppSettings()

app = FastAPI(
    docs_url=app_settings.docs_url or None,
    openapi_url=app_settings.openapi_url or None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=app_settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "Output-Filename"],
)

if app_settings.app_tag == "dev":
    app.add_middleware(SQLAlchemyMiddleware)

app.add_middleware(RouterLoggingMiddleware)

Base.metadata.create_all(engine)


@app.get("/ping")
async def pong():
    """Sanity check.

    This will let the user know that the service is operational.
    And this path operation will:
    * show a lifesign
    """
    return {"ping": "pong!"}


"""
docker
docker-compose


"""
