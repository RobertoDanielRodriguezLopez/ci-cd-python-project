from fastapi import APIRouter

router = APIRouter(tags=["default"])


@router.get("/health")
def health_check():
    return {"status": "ok"}
