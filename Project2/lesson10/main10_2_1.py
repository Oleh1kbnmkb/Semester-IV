from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="2489721567912457812")

@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_name = form_data.username
    password = form_data.password

    if user_name != "admin" or password != "secret":
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user_name, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    if token != "admin":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"user": token}


if __name__ == "__main__":
  uvicorn.run("main10_2_1:app", host="127.0.0.1", reload=True)