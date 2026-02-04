from fastapi import APIRouter

from app.api.v1.endpoints import (
    accounting,
    inventory,
    manufacturing,
    mes,
    planning,
    quality,
    sales,
)

api_router = APIRouter()
api_router.include_router(manufacturing.router, prefix="/manufacturing", tags=["Manufacturing"])
api_router.include_router(planning.router, prefix="/planning", tags=["Planning"])
api_router.include_router(mes.router, prefix="/mes", tags=["MES"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
api_router.include_router(quality.router, prefix="/quality", tags=["Quality"])
api_router.include_router(accounting.router, prefix="/accounting", tags=["Accounting"])
api_router.include_router(sales.router, prefix="/sales", tags=["Sales"])
