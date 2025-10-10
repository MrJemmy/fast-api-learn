from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class BaseBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class Book(BaseBook):
    id: int
    published_date: str


books: list[Book] = [
    Book(id=1,
         title="Dune",
         author="Frank Herbert",
         publisher="Chilton Books",
         published_date="1965-8-1",
         page_count=412,
         language="English"
         ),
    Book(id=2,
         title="The Name of the Wind",
         author="Patrick Rothfuss",
         publisher="DAW Books",
         published_date="2007-3-27",
         page_count=662,
         language="English"
         )
]


@app.get(
    "/books",
    response_model=dict[str, list[Book]],
    status_code=status.HTTP_200_OK
)
async def get_all_books() -> dict[str, list[Book]]:
    return {"books": books}


@app.get(
    "/book/{book_id}",
    response_model=dict[str, Book],
    status_code=status.HTTP_200_OK
)
async def get_book(book_id: int) -> dict[str, Book]:
    for book in books:
        if book.id == book_id:
            return {"book": book}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@app.post(
    "/book",
    response_model=dict[str, Book],
    status_code=status.HTTP_201_CREATED
)
async def create_book(book_data: Book) -> dict[str, Book]:
    # new_book = book_data.model_dump()
    books.append(book_data)
    return {"book": book_data}


@app.put(
    "/book/{book_id}",
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


@app.delete(
    "/book/{book_id}",
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
