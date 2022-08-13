from fastapi import APIRouter, Depends
from sqlmodel import select

from core.db import AsyncSession, get_session
from models import UserCreate, UserToken, User

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    user = (await session.execute(select(User).where(User.id == user_data.id))).scalar_one_or_none()

    if not user:
        user = User(
            id=user_data.id, bdate=user_data.bdate, photo_100=user_data.photo_100, photo_200=user_data.photo_200,
            photo_max_orig=user_data.photo_max_orig, first_name=user_data.first_name, last_name=user_data.last_name,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

    token = UserToken(user_id=user_data.id)
    session.add(token)
    await session.commit()
    await session.refresh(token)

    return token.token
