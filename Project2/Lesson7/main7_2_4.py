from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, FieldValidationInfo, field_validator
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

    @field_validator('price')
    def price_must_be_positive(cls, value: float, info: FieldValidationInfo):
        if value <= 0:
            raise ValueError('Ціна має бути більшою за нуль')
        return value

@app.post("/items/")
def create_item(item: Item):
    return item



if __name__ == "__main__":
  uvicorn.run("main7_2_4:app", host="127.0.0.1", reload=True)