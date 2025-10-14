from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine
from ..config import settings


engine = AsyncEngine(
    create_engine(
        url=settings.DATABASE_URL,
        echo=True
    )
)
