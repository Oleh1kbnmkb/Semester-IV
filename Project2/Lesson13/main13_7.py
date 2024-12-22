from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
  print(f"Запит: {request.method} {request.url}")
  response = await call_next(request)
  print(f"Відповідь: {response.status_code}")
  return response
