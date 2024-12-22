from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    country: Optional[str] = None



@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{item_id}")
async def get_item(item_id: int, name: Optional[str] = None):
    return {"item_id": item_id, "name": name}



if __name__ == "__main__":
  uvicorn.run("main7_1:app", host="127.0.0.1", reload=True)