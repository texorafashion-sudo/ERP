from fastapi import APIRouter

router = APIRouter()


@router.get("/pipeline")
async def sales_pipeline():
    return {
        "open_quotes": 14,
        "open_orders": 9,
        "on_time_delivery": 96.2,
    }
