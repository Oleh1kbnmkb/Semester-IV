from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.middleware("http")
async def global_middleware(request: Request, call_next):
    response = await call_next(request)
    return response



if __name__ == "__main__":
  uvicorn.run("main13_3:app", host="127.0.0.1", reload=True)