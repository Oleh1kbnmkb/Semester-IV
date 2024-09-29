from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()




@app.get('/items')
async def get_items():
  return {"message": "All Items"}



@app.get('/items/{item_id}')
async def get_item(item_id: int):
  return {"message": f"Get item {item_id}"}



@app.get('/items/name/{item_id}')
async def item_name(item_id: int):
  return {"name": f"Item {item_id} name"}


@app.get('/item/price/{item_id}')
async def item_price(item_id: int):
  return {"price": f"Item price {item_id}"}




@app.get('/item/tax/{item_id}')
async def item_tax(item_id: int):
  return {"price": f"Item tax {item_id}"}

class Item(BaseModel):
  name: str
  price: float


@app.post("/items/")
async def create_item(item: Item):
  return {"message": f"Item {item.name} created with price {item.price}"}


@app.post("/items/{item_id}")
async def create_specific_item(item_id: int, item: Item):
  return {"message": f"Item {item_id} created with name {item.name}"}


@app.post("/items/{item_id}/name")
async def set_item_name(item_id: int, name: str):
  return {"message": f"Item {item_id} name set to {name}"}


@app.post("/items/{item_id}/price")
async def set_item_price(item_id: int, price: float):
  return {"message": f"Item {item_id} price set to {price}"}


@app.post("/items/{item_id}/tax")
async def set_item_tax(item_id: int, tax: float):
  return {"message": f"Item {item_id} tax set to {tax}"}





@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

@app.delete("/items/all")
async def delete_all_items():
    return {"message": "All items deleted"}

@app.delete("/items/{item_id}/name")
async def delete_item_name(item_id: int):
    return {"message": f"Item {item_id} name deleted"}

@app.delete("/items/{item_id}/price")
async def delete_item_price(item_id: int):
    return {"message": f"Item {item_id} price deleted"}

@app.delete("/items/{item_id}/tax")
async def delete_item_tax(item_id: int):
    return {"message": f"Item {item_id} tax deleted"}




@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} updated with name {item.name} and price {item.price}"}

@app.put("/items/{item_id}/name")
async def update_item_name(item_id: int, name: str):
    return {"message": f"Item {item_id} name updated to {name}"}

@app.put("/items/{item_id}/price")
async def update_item_price(item_id: int, price: float):
    return {"message": f"Item {item_id} price updated to {price}"}

@app.put("/items/{item_id}/tax")
async def update_item_tax(item_id: int, tax: float):
    return {"message": f"Item {item_id} tax updated to {tax}"}

@app.put("/items/{item_id}/description")
async def update_item_description(item_id: int, description: str):
    return {"message": f"Item {item_id} description updated to {description}"}





@app.patch("/items/{item_id}")
async def partial_update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} partially updated with {item}"}

@app.patch("/items/{item_id}/name")
async def partial_update_item_name(item_id: int, name: str):
    return {"message": f"Item {item_id} name updated to {name}"}

@app.patch("/items/{item_id}/price")
async def partial_update_item_price(item_id: int, price: float):
    return {"message": f"Item {item_id} price updated to {price}"}

@app.patch("/items/{item_id}/tax")
async def partial_update_item_tax(item_id: int, tax: float):
    return {"message": f"Item {item_id} tax updated to {tax}"}

@app.patch("/items/{item_id}/description")
async def partial_update_item_description(item_id: int, description: str):
    return {"message": f"Item {item_id} description updated to {description}"}




if __name__ == "__main__":
  uvicorn.run("main1_home:app", host="127.0.0.1", reload=True)