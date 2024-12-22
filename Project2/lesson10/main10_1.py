from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Для простоти, збережемо токен в пам'яті
fake_tokens = {"секретнийтокен": "admin"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token not in fake_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невірний токен",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": fake_tokens[token]}

@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "secret":
        # Повертаємо фіксований токен
        access_token = "секретнийтокен"
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неправильні облікові дані",
        headers={"WWW-Authenticate": "Bearer"},
    )

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}


if __name__ == "__main__":
  uvicorn.run("main10_1:app", host="127.0.0.1", reload=True)