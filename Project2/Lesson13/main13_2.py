from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.middleware("http")
async def log_requests(request: Request, call_next):
    detail = f"Запит: {request.method} на URL: {request.url}"
    response = await call_next(request)
    print(detail)
    return response

@app.get("/")
async def read_root():
    return {"message": "Привіт Світ"}

if __name__ == "__main__":
  uvicorn.run("main13_2:app", host="127.0.0.1", reload=True)