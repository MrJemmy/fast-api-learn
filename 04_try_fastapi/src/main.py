import os
from fastapi import FastAPI
from typing import Union
from src.config import settings

app = FastAPI()


@app.get("/healthz")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/")
def env_var():
    return {
        "PORT": os.getenv("PORT", "Not Found"), 
        "DATABASE_URL": os.getenv("DATABSE_URL", "Not Found"), 
        "POSTGRES_USER": os.getenv("POSTGRES_USER", "Not Found"), 
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD", "Not Found"), 
        "POSTGRES_DB": os.getenv("POSTGRES_DB", "Not Found")
        }

@app.get("/config")
def config_env_var():
    return {
        "DATABASE_URL": settings.DATABASE_URL
        }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

