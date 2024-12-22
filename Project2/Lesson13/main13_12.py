from fastapi import FastAPI, Request, Response
from typing import Callable
import uvicorn

app = FastAPI()
def middleware_factory(header_name: str, header_value: str):
    async def custom_middleware(request: Request, call_next: Callable):
        response: Response = await call_next(request)
        response.headers[header_name] = header_value
        return response
    return custom_middleware

app.middleware("http")(middleware_factory("X-Custom-Header", "MyValue"))
app.middleware("http")(middleware_factory("X-Another-Header", "AnotherValue"))

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
  uvicorn.run("main13_12:app", host="127.0.0.1", reload=True)