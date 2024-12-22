from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, FieldValidationInfo, field_validator, ValidationError
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    @field_validator('price')
    def price_must_be_positive(cls, value: float, info: FieldValidationInfo):
        if value <= 0:
            raise ValueError('Price must be positive')
        return value

@app.post("/items/")
def create_item(item: Item):
    try:
        return item
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())



if __name__ == "__main__":
  uvicorn.run("main7_2_3:app", host="127.0.0.1", reload=True)