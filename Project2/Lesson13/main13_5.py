from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.middleware("http")
async def async_middleware(request: Request, call_next):
  print("Мiddleware виконується перед обробкою запиту")
  response = await call_next(request)
  print("Мiddleware виконується після обробки запиту")

  return response


@app.get("/")
async def root():
  return {"message": "Hello, World!"}



if __name__ == "__main__":
  uvicorn.run("main13_5:app", host="127.0.0.1", reload=True)