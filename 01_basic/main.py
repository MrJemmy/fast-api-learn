from fastapi import FastAPI, Header, Request
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def home() -> dict:
    return {"msg": "Hello world"}


@app.get("/query")
async def query_params(name: str) -> dict:
    return {"msg": f"Hello {name}"}


@app.get("/query_optional")
async def query_optional(name: str, age: Optional[int] = None) -> dict:
    return {"msg": f"Hello {name}, and your age is {age}"}


@app.get("/dynamic/{name}")
async def dynamic_url(name: str) -> dict:
    return {"msg": f"Hello {name}"}


@app.get("/mix/{name}")
async def query_dynamic(name: str, age: int) -> dict:
    return {"msg": f"Hello {name}, and your age is {age}"}


class BodyData(BaseModel):
    title: str
    desc: str


@app.post("/body")
async def body_data(body_data: BodyData) -> dict:
    return {
        "data": body_data
    }


@app.get("/header")
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
) -> dict:

    req_header = {}
    req_header["Accept"] = accept
    req_header["Content-Type"] = content_type
    req_header["User-Agent"] = user_agent
    req_header["HOST"] = host

    return {
        "header": req_header
    }


@app.get("/request")
async def get_request(request: Request) -> dict:

    req_header = {}

    forwarded_for = request.headers.get("X-Forwarded-For")

    real_ip = (
        forwarded_for.split(",")[0]
        if forwarded_for
        else request.client.host if request.client is not None else None
    )

    req_header["ip"] = real_ip
    req_header["user_agent"] = request.headers.get("user-agent")
    req_header["user_agent"] = request.headers.get("user-agent")
    req_header["language"] = request.headers.get("accept-language"),
    req_header["origin"] = request.headers.get("origin"),
    req_header["referer"] = request.headers.get("referer"),
    req_header["content_type"] = request.headers.get("Content-Type"),
    req_header["accept"] = request.headers.get("Accept"),
    return {
        "header": req_header
    }
