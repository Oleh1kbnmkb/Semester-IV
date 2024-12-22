from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.middleware("http")
async def authenticate_request(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token or not validate_token(token):
        return JSONResponse(status_code=401, content={"detail": "Invalid or missing token"})

    response = await call_next(request)
    return response

def validate_token(token: str) -> bool:
    return token == "Ithinkitshouldbesometoken"

@app.get("/secure-endpoint")
def secure_endpoint():
    return {"message": "Secure Endpoint"}


if __name__ == "__main__":
  uvicorn.run("main10_2_4:app", host="127.0.0.1", reload=True)