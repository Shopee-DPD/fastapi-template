from fastapi import APIRouter

health_router = APIRouter(prefix="/ping", tags=["Health Check"])


@health_router.get("")
async def health_check():
    return "pong!"
