from typing import Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/kong-request-id")
async def get_kong_request_id(kong_request_id: Optional[str] = Header(None)):
    return {"Kong-Request-ID": kong_request_id}
