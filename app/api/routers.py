from fastapi import APIRouter
from app.api.endpoints import auth, users

# from app.api.endpoints import

router = APIRouter()

# router.include_router()
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(users.router, prefix="/users", tags=["Users"])
