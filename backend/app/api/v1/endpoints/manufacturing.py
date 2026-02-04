from fastapi import APIRouter

router = APIRouter()


@router.get("/overview")
async def manufacturing_overview():
    return {
        "active_work_orders": 12,
        "open_sales_orders": 7,
        "bom_count": 54,
    }
