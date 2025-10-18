from sqlmodel.ext.asyncio.session import AsyncSession
from .model import Book
from .schemas import BaseBook
from sqlmodel import select


class BookService:
    async def get_books(self, session: AsyncSession):
        statement = select(Book)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_book(self, session: AsyncSession, book_id: int):
        statement = select(Book).where(Book.id == book_id)
        result = await session.execute(statement)
        book = result.scalars().one_or_none()
        return book

    async def create_book(self, session: AsyncSession, book_data: BaseBook):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
        return new_book

    async def update_book(
        self, session: AsyncSession, book_id: int, book_data: BaseBook
    ):
        book_to_update = await self.get_book(session, book_id)

        if book_to_update is None:
            return None

        update_data = book_data.model_dump()

        for key, value in update_data.items():
            setattr(book_to_update, key, value)

        await session.commit()

        return book_to_update

    async def delete_book(self, session: AsyncSession, book_id: int):
        book_to_delete = await self.get_book(session, book_id)

        if book_to_delete is None:
            return None

        await session.delete(book_to_delete)
        await session.commit()
