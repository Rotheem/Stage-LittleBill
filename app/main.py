"""File defining the Metadata. And the basic functions creating the database tables and calling the router"""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.settings import Settings
from app.log import LogConfig

from app.endpoints import router

# NOTE: We can not get loggers at the top of this file like we do in other files
# as the loggers are not yet initialized


def use_route_path_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function names.

    Theses names may be used by API clients to generate function names.
    The operation_id will have the format "method_path", like "get_users_me".

    See https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            # The operation_id should be unique.
            # It is possible to set multiple methods for the same endpoint method but it's not considered a good practice.
            method = "_".join(route.methods)
            route.operation_id = method.lower() + route.path.replace("/", "_")


def init_db(
    settings: Settings,
    logger: logging.Logger,
    drop_db: bool = False,
) -> None:
    """
    Init the database by creating the tables and adding the necessary groups

    The method will use a synchronous engine to create the tables and add the groups
    """
    pass


# We wrap the application in a function to be able to pass the settings and drop_db parameters
# The drop_db parameter is used to drop the database tables before creating them again
def get_application(settings: Settings) -> FastAPI:
    # Initialize loggers
    LogConfig().initialize_loggers(settings=settings)
    logger = logging.getLogger("hyperion")

    # Create folder for calendars if they don't already exists
    Path("data/ics/").mkdir(parents=True, exist_ok=True)
    Path("data/core/").mkdir(parents=True, exist_ok=True)

    # Creating a lifespan which will be called when the application starts then shuts down
    # https://fastapi.tiangolo.com/advanced/events/
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator:
        yield
        logger.info("Shutting down")

    # Initialize app
    app = FastAPI(
        title="Hyperion",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.include_router(router)
    use_route_path_as_operation_ids(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_application(settings=Settings())  # type: ignore
