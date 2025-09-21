
from fastapi import APIRouter, Request
from ..rate_limiter import limiter, RateLimitConfig

router = APIRouter(prefix="/test", tags=["warehouses"])

@router.get("/")
@limiter.limit(RateLimitConfig.READ)
async def get(request: Request):
    return {
        "detail": "Hello world"
    }
