# we can put this file into __init__.py also so when we load book or projecte
# folder or any sub folder it load automaticaly this code

from fastapi import FastAPI
from .book import router as book_router
from fastapi.middleware.cors import CORSMiddleware

version = "v1"

app = FastAPI(
    title="Book CRUD",
    description="A REST API for a book review web service",
    version=version
)
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

app.include_router(book_router, prefix=f"/api/{version}/book")
