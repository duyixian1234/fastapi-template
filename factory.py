import importlib
import logging

from fastapi import APIRouter, FastAPI

logger = logging.getLogger(__name__)


def create_app(**kwargs) -> FastAPI:
    return FastAPI(**kwargs)


def register_routers(app: FastAPI, view_module: str) -> None:
    views_modules = importlib.import_module(view_module)
    logger.info("Register Routers From <%s>", views_modules.__name__)
    for attr_name in dir(views_modules):
        attr = getattr(views_modules, attr_name)
        if isinstance(attr, APIRouter):
            app.include_router(attr, tags=[attr_name])
            logger.info("Register Router <%s>", attr_name)
