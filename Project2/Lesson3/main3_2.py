from fastapi import FastAPI
from databases import Database
import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Підключення до бази даних
DATABASE_URL = "sqlite:///./example.db"

# SQLAlchemy engine та метадані
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Ініціалізація бази даних для асинхронного використання
database = Database(DATABASE_URL)

# Ініціалізація FastAPI
app = FastAPI()

# Оголошення таблиці users
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

# Створення таблиць
metadata.create_all(engine)

# Підключення до бази під час старту сервера
@app.on_event("startup")
async def startup():
    await database.connect()

# Відключення від бази під час вимкнення сервера
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Ендпоінт для отримання користувача за його id
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user:
        return {"user": dict(user)}
    return {"error": "User not found"}


if __name__ == "__main__":
  uvicorn.run("main3_2:app", host="127.0.0.1", reload=True)

