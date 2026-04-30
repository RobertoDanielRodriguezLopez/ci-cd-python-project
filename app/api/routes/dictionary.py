from fastapi import APIRouter
from pydantic import BaseModel
from app.dictionary.dictionary import Dictionary

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

dictionary = Dictionary()


class DictionaryRequest(BaseModel):
    word: str
    definition: str


@router.post("")
def add_entry(payload: DictionaryRequest):
    dictionary.newentry(payload.word, payload.definition)
    return {"word": payload.word, "definition": payload.definition}


@router.get("/{word}")
def get_entry(word: str):
    result = dictionary.Look(word)
    return {"result": result}
