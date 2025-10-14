from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Provide a default or ensure .env has DATABASE_URL
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"


settings = Settings()
