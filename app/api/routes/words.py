from fastapi import APIRouter
from pydantic import BaseModel
from app.words.word_builder import build_word

router = APIRouter(prefix="/build-word", tags=["words"])


class BuildWordRequest(BaseModel):
    words: list[str]


@router.post("")
def build(payload: BuildWordRequest):
    result = build_word(payload.words)
    return {"result": result}
