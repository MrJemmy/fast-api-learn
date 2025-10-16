from pydantic import BaseModel
from datetime import datetime


class BaseBook(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class Book(BaseBook):
    id: int
