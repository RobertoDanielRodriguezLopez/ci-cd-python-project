from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.dictionary import router as dictionary_router
from app.api.routes.calculator import router as calculator_router
from app.api.routes.words import router as words_router

app = FastAPI(
    title="CI/CD Python Project API",
    description="API layer for the CI/CD Python Project",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(dictionary_router)
app.include_router(calculator_router)
app.include_router(words_router)
