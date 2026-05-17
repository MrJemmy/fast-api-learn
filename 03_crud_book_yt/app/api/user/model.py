from typing import Optional, ClassVar, List, TYPE_CHECKING
from sqlmodel import (
    SQLModel, Field, Column, DateTime, Relationship)
from sqlalchemy.sql import func
from datetime import datetime
import pytz


# Assuming TIMEZONE is accessible (e.g., imported from a config file)
TIMEZONE = pytz.timezone("Asia/Kolkata")

if TYPE_CHECKING:
    from app.api.book.model import Book


class User(SQLModel, table=True):
    __tablename__: ClassVar[str] = "users"  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)

    email: str = Field(nullable=False, unique=True, index=True)
    username: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)

    # added latter on
    first_name: str = Field(nullable=True)
    last_name: str = Field(nullable=True)
    Address: str = Field(nullable=True)

    # created_at: datetime = Field(default_factory=datetime.utcnow) # find solution to conver time based on users timezone
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True), default=func.now())
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIMEZONE),
        sa_column=Column(DateTime(timezone=True),
                         default=func.now(), onupdate=func.now())
    )

    books: List["Book"] = Relationship(back_populates="owner")

    is_deleted: bool = Field(default=False, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"
