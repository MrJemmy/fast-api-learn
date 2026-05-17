from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.db.config import get_session

from app.api.book.model import Book
from app.api.book.schemas import BaseBook
from app.api.book.services import BookService

router = APIRouter()
book_service = BookService()


@router.get(
    "/",
    response_model=dict[str, List[Book]],
    status_code=status.HTTP_200_OK
)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    try:
        books = await book_service.get_books(session)
        print("books :", books)
        return {"books": books}
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )

@router.get(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):

    try:
        book = await book_service.get_book(book_id, session)
        if book:
            return {"book": book}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )

@router.post(
    "/",
    response_model=dict[str, Book],
    status_code=status.HTTP_201_CREATED
)
async def create_book(
        book_data: BaseBook,
        session: AsyncSession = Depends(get_session)):
    try:
        # new_book = book_data.model_dump()
        book = await book_service.create_book(book_data, session)
        return {"book": book}
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )



@router.put(
    "/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def update_book(
        book_id: int,
        book_data: BaseBook,
        session: AsyncSession = Depends(get_session)):
    try:
        updated_book = await book_service.update_book(
            book_id, book_data, session)
        if updated_book:
            return {"book": updated_book}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book(
        book_id: int,
        session: AsyncSession = Depends(get_session)) -> None:
    try:
        deleted_book = await book_service.delete_book(book_id, session)
        if deleted_book:
            return
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed : {str(e)}"
        )
    except  Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Something went wrong, please try again later: {str(e)}"
        )
