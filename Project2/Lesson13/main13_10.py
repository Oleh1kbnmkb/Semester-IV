from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()


@app.middleware("http")
async def xss_protect(request: Request, call_next):
  response = await call_next(request)
  response.headers["Content-Security-Policy"] = "default-src 'self'"

  return response
