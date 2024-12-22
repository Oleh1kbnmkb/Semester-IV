from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()


@app.get("/", summary="Головна сторінка", tags=["General"])
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/items/", summary="Отримання списку елементів", tags=["Items"])
async def get_items(skip: int = 0, limit: int = 10):
    items = [{"item_id": i, "name": f"Item {i}"} for i in range(skip, skip + limit)]
    return items


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/", summary="Створення нового елемента", tags=["Items"])
async def create_item(item: Item):
    return {"name": item.name, "price": item.price, "tax": item.tax}


@app.put("/items/{item_id}", summary="Оновлення існуючого елемента", tags=["Items"])
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


@app.delete("/items/{item_id}", summary="Видалення елемента", tags=["Items"])
async def delete_item(item_id: int):
    return {"message": f"Item with id {item_id} has been deleted"}


if __name__ == "__main__":
  uvicorn.run("main11_home:app", host="127.0.0.1", reload=True)