from fastapi import FastAPI, Depends, HTTPException, status, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Simulated database of tokens and their associated user data
USERS_DB = {
    "user1_token": {"username": "user1", "role": "user"},
    "admin_token": {"username": "admin", "role": "admin"}
}

class User(BaseModel):
    username: str
    role: str

def authenticate_user(token: str) -> User:
    """Authenticate the user based on the token."""
    user_data = USERS_DB.get(token)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authorization token"
        )
    return User(**user_data)

def get_current_user(request: Request) -> User:
    """Extract and validate the current user from the Authorization header."""
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header is missing"
        )
    return authenticate_user(token)

@app.get("/admin")
def admin_route(user: User = Depends(get_current_user)):
    """Admin-only endpoint."""
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Admins only"
        )
    return {"message": f"Welcome, {user.username}!"}

@app.get("/user")
def user_route(user: User = Depends(get_current_user)):
    """User endpoint."""
    return {"message": f"Welcome, {user.username}!"}




if __name__ == "__main__":
  uvicorn.run("main13_11:app", host="127.0.0.1", reload=True)