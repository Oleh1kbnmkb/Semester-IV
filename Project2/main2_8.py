import uvicorn
from databases import Database
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String, unique=True)  # Add unique constraint
)
metadata.create_all(engine)

database = Database(DATABASE_URL)


# Lifespan handler for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
  # Startup logic
  await database.connect()
  yield
  # Shutdown logic
  await database.disconnect()


app = FastAPI(lifespan=lifespan)


# Route to create a new user
@app.post("/users/{user_name}")
async def create_user(user_name: str):
  query = users.select().where(users.c.name == user_name)
  existing_user = await database.fetch_one(query)

  if existing_user:
    raise HTTPException(status_code=400, detail="User with this name already exists")

  query = users.insert().values(name=user_name)
  await database.execute(query)

  return {"user_name": user_name}


# Route to read all users
@app.get("/users")
async def read_users():
  query = users.select()
  all_users = await database.fetch_all(query)

  # Serialize list of users to simple dictionary format
  return {"users": [{"id": user["id"], "name": user["name"]} for user in all_users]}


# Run the app with Uvicorn
if __name__ == "__main__":
  uvicorn.run("main2_8:app", host="127.0.0.1", reload=True)
