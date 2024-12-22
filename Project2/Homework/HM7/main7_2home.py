from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
import uvicorn
import re

app = FastAPI()


class User(BaseModel):
    first_name: str = Field(min_length=2, pattern="^[A-Za-z]+$")
    last_name: str = Field(min_length=2, pattern="^[A-Za-z]+$")
    email: EmailStr
    password: str
    phone: str


def validate_password(password: str):
    if (len(password) < 8 or not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password) or
        not re.search(r'[!@#\$%\^&\*]', password)):
        raise HTTPException(status_code=400, detail="Password does not meet the requirements.")


def validate_phone(phone: str):
    phone_regex = r'^\+?\d{10,15}$'
    if not re.match(phone_regex, phone):
        raise HTTPException(status_code=400, detail="Invalid phone number.")


@app.post("/register", status_code=201)
def register_user(user: User):
    validate_password(user.password)
    validate_phone(user.phone)
    return {"message": "User registered successfully!"}



if __name__ == "__main__":
  uvicorn.run("main7_2home:app", host="127.0.0.1", reload=True)