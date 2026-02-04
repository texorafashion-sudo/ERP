from fastapi import APIRouter

router = APIRouter()


@router.get("/live")
async def mes_live():
    return {
        "lines_running": 4,
        "oee": 82.4,
        "downtime_events": 2,
    }
