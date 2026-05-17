from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.user.model import User
from app.api.user.schemas import UserUpdateSchema


class UserService:
    async def get_users(self, session: AsyncSession):
        statement = select(User).where(User.is_deleted == False)
        result = await session.execute(statement)
        return result.scalars().all()
    
    async def get_user_by_id(self, user_id: int, session: AsyncSession):
        statement = select(User).where(User.id == user_id, User.is_deleted == False)
        result = await session.execute(statement)
        user = result.scalars().one_or_none()
        return user

    async def get_user_by_username(self, username: str, session: AsyncSession):
        statement = select(User).where(User.username == username, User.is_deleted == False)
        result = await session.execute(statement)
        user = result.scalars().one_or_none()
        return user

    async def update_user(self, user_id: int, user_data: UserUpdateSchema, session: AsyncSession):
        user = await self.get_user_by_id(user_id, session)

        if user is None:
            return None

        # Example update logic (this should be replaced with actual update data)
        user.first_name = user_data.first_name if user_data.first_name else user.first_name
        user.last_name = user_data.last_name if user_data.last_name else user.last_name
        user.Address = user_data.Address if user_data.Address else user.Address

        # almost same result as above check
        # update_data = user_data.model_dump()
        # for key, value in update_data.items():
        #     setattr(user, key, value)

        await session.commit()

        return user
    
    async def delete_user(self, user_id: int, session: AsyncSession):
        user = await self.get_user_by_id(user_id, session)

        if user is None:
            return None

        user.is_deleted = True
        await session.commit()
        return user