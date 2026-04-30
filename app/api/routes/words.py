from fastapi import APIRouter
from pydantic import BaseModel
from app.words.word_builder import build_word

router = APIRouter(prefix="/build-word", tags=["words"])


# ---------
# Request
# ---------
class BuildWordRequest(BaseModel):
    words: list[str]

    class Config:
        json_schema_extra = {
            "example": {
                "words": ["yoda", "best", "has"]
            }
        }


# ----------
# Response
# ----------
class BuildWordResponse(BaseModel):
    result: str


@router.post("", response_model=BuildWordResponse)
def build(payload: BuildWordRequest):
    result = build_word(payload.words)
    return {"result": result}
