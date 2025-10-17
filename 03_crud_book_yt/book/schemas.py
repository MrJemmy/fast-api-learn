from pydantic import BaseModel
from datetime import datetime


class BaseBook(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str


class Book(BaseBook):
    id: int
    created_at: datetime
    updated_at: datetime
