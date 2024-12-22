from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


fake_items_db = [{"item": f"Item {i}"} for i in range(100)]

def get_items_from_database(skip: int, limit: int):
    return fake_items_db[skip : skip + limit]

def search_items_in_database(query: str):
    return [item for item in fake_items_db if query.lower() in item["item"].lower()]

@app.get("/items/")
async def read_items(skip: int = Query(0, title="Пропустити", description="Кількість записів для пропуску"),
                    limit: int = Query(10, title="Ліміт", description="Максимальна кількість записів для видачі")):
    items = get_items_from_database(skip, limit)
    return {"items": items}

@app.get("/search/")
async def search_items(query: str = Query(..., title="Пошук", description="Запит для пошуку елементів")):
    items = search_items_in_database(query)
    return {"items": items}


if __name__ == "__main__":
  uvicorn.run("main5_2:app", host="127.0.0.1", reload=True)