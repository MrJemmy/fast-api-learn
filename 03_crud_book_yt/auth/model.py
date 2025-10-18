from typing import Optional, ClassVar, List
from sqlmodel import (
    SQLModel, Field, Column, DateTime, Relationship, UniqueConstraint)
from sqlalchemy.sql import func
from datetime import datetime
import pytz
from ..book.model import Book

# Assuming TIMEZONE is accessible (e.g., imported from a config file)
TIMEZONE = pytz.timezone("Asia/Kolkata")


class User(SQLModel, table=True):
    __tablename__: ClassVar[str] = "users"  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)

    email: str = Field(nullable=False, unique=True, index=True)
    username: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True),
                         default=func.now(), onupdate=func.now())
    )

    books: List[Book] = Relationship(back_populates="owner")

    __table_args__ = (
        UniqueConstraint("email"),
        UniqueConstraint("username")
    )

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"
