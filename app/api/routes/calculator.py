from fastapi import APIRouter
from pydantic import BaseModel
from app.shopping.cost_calculator import get_total

router = APIRouter(prefix="/calculate-total", tags=["calculator"])


# ---------
# Request
# ---------
class CalculateTotalRequest(BaseModel):
    costs: dict
    items: list
    tax: float

    class Config:
        json_schema_extra = {
            "example": {
                "costs": {"socks": 5, "shoes": 60},
                "items": ["socks", "shoes"],
                "tax": 0.09
            }
        }


# ----------
# Response
# ----------
class CalculateTotalResponse(BaseModel):
    total: float


@router.post("", response_model=CalculateTotalResponse)
def calculate_total(payload: CalculateTotalRequest):
    total = get_total(payload.costs, payload.items, payload.tax)
    return {"total": total}
