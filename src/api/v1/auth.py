from fastapi import APIRouter
from models import UserCreate, UserToken


router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(user_data: UserCreate):
    return user_data
