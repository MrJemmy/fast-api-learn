from typing import AsyncGenerator
from sqlalchemy import text
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
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1;"))
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
