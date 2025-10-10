from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class Book(BaseBook):
    id: int
    published_date: str
