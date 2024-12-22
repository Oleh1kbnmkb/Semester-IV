from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

def is_valid_csrf(token: str) -> bool:

    return token == "valid_csrf_token"

@app.middleware("http")
async def csrf_protect(request: Request, call_next):
    if request.method in ["POST", "PUT", "DELETE"]:
        csrf_token = request.headers.get("X-CSRF-Token")
        if not csrf_token or not is_valid_csrf(csrf_token):
            return JSONResponse(status_code=403, content={"detail": "CSRF token missing or invalid"})

    response = await call_next(request)
    return response


if __name__ == "__main__":
  uvicorn.run("main13_9:app", host="127.0.0.1", reload=True)