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
sample_books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "novel", "rating": 4.3},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "novel", "rating": 4.8},
    {"title": "1984", "author": "George Orwell", "genre": "dystopian", "rating": 4.2},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "dystopian", "rating": 4.5}
]

# Фільтрація загальних даних
def filter_data(data, **filters):
    for key, value in filters.items():
        if value is not None:
            data = [item for item in data if item.get(key) == value or item.get(key) >= value or item.get(key) <= value]
    return data

# Маршрут для отримання елементів з пагінацією
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"items": fake_items_db[skip: skip + limit]}

# Маршрут для пошуку елементів
@app.get("/search/")
async def search_items(query: str):
    return {"items": [item for item in fake_items_db if query.lower() in item["item"].lower()]}

# Маршрут для отримання користувачів з пагінацією
@app.get("/users/")
async def get_users(skip: int = 0, limit: int = 10):
    return {"users": fake_users_db[skip: skip + limit]}

# Маршрут для отримання елементів з фільтром
@app.get("/items/filter/")
async def read_items_filter(q: Optional[str] = None):
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

# Маршрут для отримання рекомендацій книг
@app.get("/book-recommendations/")
async def get_book_recommendations(
    genre: str,
    min_rating: float = Query(4.0, gt=0, le=5)
):
    return {"books": fetch_book_recommendations(genre, min_rating)}

# Функція для фільтрації книг за жанром і рейтингом
def fetch_book_recommendations(genre: str, min_rating: float):
    return [book for book in sample_books if book["genre"] == genre and book["rating"] >= min_rating]



if __name__ == "__main__":
  uvicorn.run("main5_6:app", host="127.0.0.1", reload=True)