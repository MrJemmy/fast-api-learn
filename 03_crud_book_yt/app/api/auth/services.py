from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.api.user.model import User
from app.api.auth.schemas import UserRegisterSchema
from app.api.auth.utils import verify_password, hash_password


class AuthService:
    async def username_exists(self, username: str, session: AsyncSession):
        statement = select(User).where(User.username == username)
        result = await session.execute(statement)
        user = result.scalars().one_or_none()
        if user:
            return True
        return False

    async def email_exists(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalars().one_or_none()
        if user:
            return True
        return False

    async def register_user(
            self, user_data: UserRegisterSchema, session: AsyncSession):
        new_user = User(username=user_data.username, email=user_data.email,
                        password=hash_password(user_data.password))
        session.add(new_user)
        await session.commit()
        return new_user


    # statement = select(User).where(
    #             ((User.username == identifier) | (User.email == identifier))
    #             & (User.is_deleted is False)
    #         )
    async def email_login(
            self, email: str, password: str, session: AsyncSession):
        statement = select(User).where(
                        (User.email == email)
                        & (User.is_deleted is False)
                    )
        result = await session.execute(statement)
        user = result.scalars().one_or_none()

        if user is None or not verify_password(password, user.password):
            return None

        return user

    async def username_login(
            self, username: str, password: str, session: AsyncSession):
        statement = select(User).where(
            (User.username == username)
            & (User.is_deleted is False)
        )
        result = await session.execute(statement)
        user = result.scalars().one_or_none()

        if not user or not verify_password(password, user.password):
            return None

        return user

