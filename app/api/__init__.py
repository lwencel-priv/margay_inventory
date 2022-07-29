from fastapi import APIRouter

from .inventory import inventory_router

router = APIRouter(prefix="/api")
router.include_router(inventory_router)
