from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


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
    return {}


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
async def update_book(book_id: int, book_data: Book) -> dict:
    return {}


@app.delete("/book/{book_id}")
async def delete_book(book_id: int) -> dict:
    return {}
