from fastapi import FastAPI, Request
from datetime import datetime
from fastapi.responses import JSONResponse
import uvicorn


app = FastAPI()


@app.middleware("http")
async def custom_middleware(request: Request, call_next):
  method = request.method
  url = request.url
  time_received = datetime.now()
  print(f"[{time_received}] HTTP Method: {method}, URL: {url}")

  if "X-Custom-Header" not in request.headers:
    return JSONResponse(
      status_code=400,
      content={"detail": "Missing X-Custom-Header"}
    )


  response = await call_next(request)
  return response



@app.get("/")
async def root():
  return {"message": "Welcome to the FastAPI application with middleware"}


@app.get("/test")
async def test_route():
  return {"message": "This is a test route"}


@app.post("/data")
async def post_data(data: dict):
  return {"received_data": data}


if __name__ == "__main__":
  uvicorn.run("main14_home:app", host="127.0.0.1", reload=True)