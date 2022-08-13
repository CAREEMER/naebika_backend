from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from starlette.status import HTTP_401_UNAUTHORIZED

from api.services.vk_api import is_valid
from core.config import app_config
from core.db import AsyncSession, get_session
from models import User, UserCreate, UserToken, VkSign

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(vk_sign: VkSign, user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    if not is_valid(vk_sign.dict(), app_config.CLIENT_SECRET):
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Wrong VK sign.")

    user = (await session.execute(select(User).where(User.id == user_data.id))).scalar_one_or_none()

    if not user:
        user = User(
            id=user_data.id,
            bdate=user_data.bdate,
            photo_100=user_data.photo_100,
            photo_200=user_data.photo_200,
            photo_max_orig=user_data.photo_max_orig,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

    token = UserToken(user_id=user_data.id)
    session.add(token)
    await session.commit()
    await session.refresh(token)

    return token.token
