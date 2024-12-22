from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError, validator
import logging
import uvicorn

app = FastAPI()

# First part: Users creation and retrieval
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

# Second part: Item retrieval with error handling
@app.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        item = get_item_from_db(item_id)
        if item is None:
            raise ValueError("Предмет не знайдено")
        return item
    except ValueError as e:
        logging.error(f"Помилка при отриманні предмета {item_id}: {str(e)}")
        return JSONResponse(
            status_code=404,
            content={"message": str(e)},
        )
    except Exception as e:
        logging.exception("Непередбачена помилка")
        return JSONResponse(
            status_code=500,
            content={"message": "Внутрішня помилка сервера"},
        )

def get_item_from_db(item_id: int):
    # Simulated database lookup. Always returns None for now.
    return None

# Third part: Item creation with validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be positive')
        return value

@app.post("/items/")
def create_item(item: Item):
    return item

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main7_2_5:app", host="127.0.0.1", reload=True)
