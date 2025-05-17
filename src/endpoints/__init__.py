from fastapi import APIRouter

from .adress import router as address_router

router = APIRouter()

router.include_router(address_router)
