from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
import uvicorn

app = FastAPI()

# Імітація бази даних
fake_items_db = [{"item": f"Item {i}"} for i in range(100)]
fake_users_db = [{"user_id": i, "name": f"User {i}"} for i in range(100)]
transactions = [
    {"account_id": 1, "date": date(2024, 9, 20), "amount": 150.00},
    {"account_id": 1, "date": date(2024, 9, 21), "amount": 250.00},
    {"account_id": 2, "date": date(2024, 9, 22), "amount": 50.00},
]

# Загальна функція для фільтрації
def filter_data(data, **filters):
    for key, value in filters.items():
        if value is not None:
            data = [item for item in data if item.get(key) == value or item.get(key) >= value or item.get(key) <= value]
    return data

# Маршрут для отримання елементів з пагінацією
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"items": fake_items_db[skip : skip + limit]}

# Маршрут для пошуку елементів
@app.get("/search/")
async def search_items(query: str):
    return {"items": [item for item in fake_items_db if query.lower() in item["item"].lower()]}

# Маршрут для отримання користувачів з пагінацією
@app.get("/users/")
async def get_users(skip: int = 0, limit: int = 10):
    return {"users": fake_users_db[skip : skip + limit]}

# Маршрут для отримання елементів з фільтром
@app.get("/items/filter/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results["filter"] = q
    return results

# Маршрут для фільтрації транзакцій
@app.get("/transactions/")
async def get_transactions(
    account_id: int,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None
):
    filters = {
        "account_id": account_id,
        "date__gte": start_date,
        "date__lte": end_date,
        "amount__gte": min_amount,
        "amount__lte": max_amount
    }
    filtered_transactions = filter_data(transactions, **filters)
    return {"transactions": filtered_transactions}


if __name__ == "__main__":
  uvicorn.run("main5_5:app", host="127.0.0.1", reload=True)