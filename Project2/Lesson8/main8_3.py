from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class ItemInput(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None

class ItemOutput(BaseModel):
  name: str
  price_with_tax: float



@app.post("/items/", response_model=ItemOutput)
def create_item(item: ItemInput):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    price_with_tax = item.price + (item.tax or 0)
    return ItemOutput(name=item.name, price_with_tax=price_with_tax)


@app.get("/items/{item_id}", response_model=ItemOutput)
def read_item(item_id: int):
    fake_db_item = {"name": "Coffee", "description": "Black hot coffee", "price": 2.5, "tax": 0.5}
    item = ItemInput(**fake_db_item)
    price_with_tax = item.price + (item.tax or 0)
    return ItemOutput(name=item.name, price_with_tax=price_with_tax)



if __name__ == "__main__":
  uvicorn.run("main8_3:app", host="127.0.0.1", reload=True)