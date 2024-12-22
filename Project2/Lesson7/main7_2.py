from fastapi import FastAPI, status, HTTPException
import uvicorn

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found")
    return {"item_id": item_id}

@app.get("/items/")
async def read_items():
    return [], status.HTTP_204_NO_CONTENT

@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"item_id": item_id, "message": "Item updated"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted"}



if __name__ == "__main__":
  uvicorn.run("main7_2:app", host="127.0.0.1", reload=True)
