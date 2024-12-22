from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

app = FastAPI()

# Correct the tokenUrl to match the /token endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Dummy token for demonstration
DUMMY_TOKEN = "dummy_token"


@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "user" and form_data.password == "password":
        return {"access_token": DUMMY_TOKEN, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    if token != DUMMY_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"user": "user", "token": token}




if __name__ == "__main__":
  uvicorn.run("main10_2:app", host="127.0.0.1", reload=True)