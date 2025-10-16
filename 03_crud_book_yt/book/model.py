from typing import Optional, ClassVar
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime
import pytz

TIMEZONE = pytz.timezone("Asia/Kolkata")


class Book(SQLModel, table=True):
    __tablename__: ClassVar[str] = "books"  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, unique=True, index=True)
    author: str
    publisher: str
    published_date: datetime = Field(sa_column=Column(
        DateTime(timezone=True), nullable=False))
    page_count: int = Field(gt=0)
    language: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True),
                         default=func.now(), onupdate=func.now())
    )

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"
