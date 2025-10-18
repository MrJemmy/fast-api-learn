from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel
from ..config import settings

engine = AsyncEngine(
    create_engine(
        url=settings.DATABASE_URL,
        echo=True
    )
)


async def init_db():
    async with engine.begin() as conn:
        from ..book.model import Book  # noqa: F401
        # await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print("result.all() : ", result.all())


async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with Session() as session:
        yield session
