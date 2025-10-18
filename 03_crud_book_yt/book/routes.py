from fastapi import APIRouter, status, HTTPException, Depends
from .model import Book
from .schemas import BaseBook
from ..db.config import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
from typing import List

router = APIRouter()
book_service = BookService()


@router.get(
    "/",
    response_model=dict[str, List[Book]],
    status_code=status.HTTP_200_OK
)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_books(session)
    print("books :", books)
    return {"books": books}


@router.get(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(session, book_id)
    if book:
        return {"book": book}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@router.post(
    "/",
    response_model=dict[str, Book],
    status_code=status.HTTP_201_CREATED
)
async def create_book(
        book_data: BaseBook,
        session: AsyncSession = Depends(get_session)):
    # new_book = book_data.model_dump()
    book = await book_service.create_book(session, book_data)
    return {"book": book}


@router.put(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def update_book(
        book_id: int,
        book_data: BaseBook,
        session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(
        session, book_id, book_data)
    if updated_book:
        return {"book": updated_book}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book(
    book_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    deleted_book = await book_service.delete_book(session, book_id)
    if deleted_book:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
