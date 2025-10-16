from fastapi import APIRouter, status, HTTPException, Depends
from .model import Book
from .schemas import BaseBook
from ..db.config import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService

router = APIRouter()
book_service = BookService()


@router.get(
    "/",
    response_model=dict[str, list[Book]],
    status_code=status.HTTP_200_OK
)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = book_service.get_books(session)
    return {"books": books}


@router.get(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book = book_service.get_book(session, book_id)
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
async def create_book(book_data: Book) -> dict[str, Book]:
    # new_book = book_data.model_dump()
    books.append(book_data)
    return {"book": book_data}


@router.put(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def update_book(book_id: int, book_data: BaseBook) -> dict:
    for book in books:
        if book.id == book_id:
            book.title = book_data.title if book_data.title else book.title
            book.author = book_data.author if book_data.author else book.author
            book.publisher = (
                book_data.publisher if book_data.publisher else book.publisher
            )
            book.page_count = (
                book_data.page_count
                if book_data.page_count
                else book.page_count
            )
            book.language = (
                book_data.language if book_data.language else book.language
            )
            return {"book": book}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@router.delete(
    "/{book_id}",
    # response_model=dict[str, Book],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(book_id: int) -> None:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )
