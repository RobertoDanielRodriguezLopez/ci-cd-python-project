from fastapi import APIRouter
from pydantic import BaseModel
from app.shopping.cost_calculator import get_total

router = APIRouter(prefix="/calculate-total", tags=["calculator"])


class CalculateTotalRequest(BaseModel):
    costs: dict
    items: list
    tax: float


@router.post("")
def calculate_total(payload: CalculateTotalRequest):
    total = get_total(payload.costs, payload.items, payload.tax)
    return {"total": total}
