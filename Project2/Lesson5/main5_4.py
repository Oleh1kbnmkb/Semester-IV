from fastapi import FastAPI, Query
from typing import Optional
import uvicorn

app = FastAPI()

# Імітація бази даних
fake_items_db = [{"item": f"Item {i}"} for i in range(100)]
fake_users_db = [{"user_id": i, "name": f"User {i}"} for i in range(100)]

# Функція для отримання елементів
def get_items_from_database(skip: int, limit: int):
    return fake_items_db[skip : skip + limit]

# Функція для пошуку елементів
def search_items_in_database(query: str):
    return [item for item in fake_items_db if query.lower() in item["item"].lower()]

# Функція для отримання користувачів
def get_users_from_database(skip: int, limit: int):
    return fake_users_db[skip : skip + limit]

# Маршрут для отримання елементів
@app.get("/items/")
async def read_items(skip: int = Query(0, title="Пропустити", description="Кількість записів для пропуску"),
                    limit: int = Query(10, title="Ліміт", description="Максимальна кількість записів для видачі")):
    items = get_items_from_database(skip, limit)
    return {"items": items}

# Маршрут для пошуку елементів
@app.get("/search/")
async def search_items(query: str = Query(..., title="Пошук", description="Запит для пошуку елементів")):
    items = search_items_in_database(query)
    return {"items": items}

# Маршрут для отримання користувачів
@app.get("/users/")
async def get_users(skip: int = Query(0, title="Пропустити", description="Кількість записів для пропуску"),
                    limit: int = Query(10, title="Ліміт", description="Максимальна кількість записів для видачі")):
    users = get_users_from_database(skip, limit)
    return {"users": users}

# Маршрут для отримання елементів з опційним фільтром
@app.get("/items/filter/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"filter": q})
    return results



if __name__ == "__main__":
  uvicorn.run("main5_4:app", host="127.0.0.1", reload=True)