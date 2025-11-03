from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.api.user.model import User
from app.api.auth.schemas import UserRegisterSchema
from app.api.auth.utils import verify_password, hash_password


class AuthService:
    async def register_user(self, user_data: UserRegisterSchema, session: AsyncSession):
        new_user = User(username=user_data.username, email=user_data.email, password=hash_password(user_data.password))
        session.add(new_user)
        await session.commit()
        return new_user
    
    async def login_user(self, identifier: str, password: str, session: AsyncSession):
        statement = select(User).where(
            ((User.username == identifier) | (User.email == identifier)) &
            (User.is_deleted == False)
        )
        result = await session.execute(statement)
        user = result.scalars().one_or_none()
        return user