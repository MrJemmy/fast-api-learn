from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession, create_async_engine, async_sessionmaker
)
from app.core.config import settings

# 1. Async engine creation
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,       # Set to True for debugging SQL statements
    future=True
)

# 2. Async session factory (sessionmaker replacement)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# 3. Dependency injection for sessions


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session  # Async context auto-closes session


# 4. DB initializer for startup
async def init_db():
    async with engine.begin():
        pass
        # from app.api.book.model import Book  # noqa: F401
        # await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print("result.all() : ", result.all())
