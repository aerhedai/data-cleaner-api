from fastapi import FastAPI
from app.api import routes
from .utils.logging import setup_logger

logger = setup_logger(__name__)
logger.info("App is starting...")
app = FastAPI(title="Python API Boilerplate")

# Register routes
app.include_router(routes.router)
