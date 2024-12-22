from fastapi import FastAPI, Path, Query
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}", summary="Отримати елемент")
async def read_item(
    item_id: int = Path(..., description="Унікальний ідентифікатор елемента"),
    q: Optional[str] = Query(None, description="Пошуковий запит")
):

    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
  uvicorn.run("main10_2:app", host="127.0.0.1", reload=True)