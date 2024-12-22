from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, condecimal, validator
from datetime import datetime
from typing import List, Optional
import uvicorn

app = FastAPI()



class Order(BaseModel):
    product_name: str = Field(..., min_length=1, description="Назва продукту не може бути порожньою")
    quantity: int = Field(1, gt=0, description="Кількість повинна бути позитивною")
    price_per_unit: condecimal(gt=0) = Field(..., description="Ціна повинна бути позитивним числом")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Дата створення замовлення")

    @validator("product_name")
    def product_name_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Назва продукту не може бути порожньою")
        return v



class User(BaseModel):
    name: str = Field(..., min_length=1, description="Ім'я користувача не може бути порожнім")
    email: EmailStr
    orders: List[Order] = []



users_db = []



@app.post("/users/", response_model=User)
def create_user(user: User):

    if any(existing_user.email == user.email for existing_user in users_db):
        raise HTTPException(status_code=400, detail="Користувач з такою електронною поштою вже існує")

    users_db.append(user)
    return user



@app.get("/users/{email}", response_model=User)
def get_user(email: EmailStr):
    user = next((user for user in users_db if user.email == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="Користувач не знайдений")
    return user


if __name__ == "__main__":
  uvicorn.run("main9_home:app", host="127.0.0.1", reload=True)