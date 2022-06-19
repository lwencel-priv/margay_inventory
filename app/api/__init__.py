from fastapi import APIRouter

from .inventory import recipe_router

router = APIRouter(prefix="/api")
router.include_router(recipe_router)
