from fastapi import FastAPI
from app.api.routes.health import router as health_router

app = FastAPI(
    title="CI/CD Python Project API",
    description="API layer for the CI/CD Python Project",
    version="1.0.0",
)

app.include_router(health_router)
