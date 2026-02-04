from fastapi import APIRouter

router = APIRouter()


@router.get("/schedule")
async def planning_schedule():
    return {
        "gantt": [],
        "bottlenecks": ["Press-02", "Paint-Line"],
    }
