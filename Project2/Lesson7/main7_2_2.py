from fastapi import FastAPI, status
import uvicorn
from pydantic import BaseModel, FieldValidationInfo, field_validator, ValidationError

app = FastAPI()

users = []


class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator('email')
    def email_must_contain_at_symbol(cls, v: str, info: FieldValidationInfo):
        if '@' not in v:
            raise ValueError('Email should contain @ symbol')
        return v


try:
    User(name="John Doe", age=30, email="johndoe")
except ValidationError as e:
    print(e.json())


if __name__ == "__main__":
    uvicorn.run("main7_2_2:app", host="127.0.0.1", reload=True)
