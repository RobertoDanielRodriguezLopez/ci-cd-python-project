from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.dictionary.dictionary import Dictionary

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

dictionary = Dictionary()


# ---------
# Request
# ---------
class DictionaryRequest(BaseModel):
    word: str
    definition: str

    class Config:
        json_schema_extra = {
            "example": {
                "word": "apple",
                "definition": "a fruit"
            }
        }


# ----------
# Response
# ----------
class DictionaryResponse(BaseModel):
    result: str


@router.post("")
def add_entry(payload: DictionaryRequest):
    dictionary.add_entry(payload.word, payload.definition)
    return {"word": payload.word, "definition": payload.definition}


@router.get(
    "/{word}",
    response_model=DictionaryResponse,
    responses={
        404: {
            "description": "Entry not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Can't find entry for banana"
                    }
                }
            },
        }
    },
)
def get_entry(word: str):
    result = dictionary.lookup(word)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Can't find entry for {word}"
        )

    return {"result": result}
