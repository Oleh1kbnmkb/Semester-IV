from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import json
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

json_data = '''
{
    "name": "Special Item",
    "description": "This is a special item",
    "price": 49.99,
    "tax": 6.0
}
'''

item_model = Item.parse_raw(json_data)
print(item_model)
print(item_model.json())



if __name__ == "__main__":
  uvicorn.run("main8_4:app", host="127.0.0.1", reload=True)
