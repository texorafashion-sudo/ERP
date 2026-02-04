from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
async def quality_metrics():
    return {
        "incoming_pass_rate": 98.4,
        "inprocess_defects": 12,
        "customer_returns": 1,
    }
