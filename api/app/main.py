from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.core.request_id import RequestIdMiddleware
from app.routers import health

configure_logging(settings.log_level)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Order and fulfillment API for the PulseCommerce platform.",
)
app.add_middleware(RequestIdMiddleware)
app.include_router(health.router)
