from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
async def inventory_summary():
    return {
        "raw_materials": 1280,
        "wip": 320,
        "finished_goods": 540,
    }
