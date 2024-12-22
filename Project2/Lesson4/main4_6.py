from fastapi import FastAPI, Form
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Participant(BaseModel):
    first_name: str
    last_name: str
    email: str

registered_participants = []

@app.post("/register/")
def register_participant(participant: Participant):
    registered_participants.append(participant)
    return {"message": f"Учасник {participant.first_name} {participant.last_name} успішно зареєстрований!"}


@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}


if __name__ == "__main__":
  uvicorn.run("main4_6:app", host="127.0.0.1", reload=True)