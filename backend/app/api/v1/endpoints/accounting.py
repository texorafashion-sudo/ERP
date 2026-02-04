from fastapi import APIRouter

router = APIRouter()


@router.get("/finance")
async def accounting_finance():
    return {
        "cash_on_hand": 128000.50,
        "monthly_revenue": 325000.00,
        "monthly_expense": 210000.00,
    }
