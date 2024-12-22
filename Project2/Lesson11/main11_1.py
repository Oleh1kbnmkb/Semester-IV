from fastapi import FastAPI, Query, Path
from typing import List, Optional
import uvicorn

app = FastAPI()

@app.get("/items/", summary="Пошук елементів")
async def search_items(
    q: Optional[List[str]] = Query(
        None,
        title="Пошукові запити",
        description="Список пошукових запитів для фільтрації елементів.",
        alias="query",
        min_length=3,
        max_length=50,
        deprecated=True
    ),
    item_id: int = Path(..., title="ID елемента", description="Унікальний ідентифікатор елемента", gt=0)
):
    return {"q": q, "item_id": item_id}


if __name__ == "__main__":
  uvicorn.run("main11_1:app", host="127.0.0.1", reload=True)