from fastapi import FastAPI, status
import uvicorn
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
  name: str
  age: int
  isEmployed: bool
  skills: list


@app.post("/user/")
def create_user(user: User):
  users.append(user)
  return user


@app.get("/users/")
def get_users():
  return users


if __name__ == "__main__":
  uvicorn.run("main7_2_1:app", host="127.0.0.1", reload=True)
