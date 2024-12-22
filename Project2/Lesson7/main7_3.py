from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()



class Book(BaseModel):
  id: int
  title: str
  author: str
  isAvailable: bool
  tags: List[str]
  metadata: Optional[dict] = None



books_db = [
  {
    "id": 1,
    "title": "Введення в алгоритми",
    "author": "Томас Кормен",
    "isAvailable": True,
    "tags": ["програмування", "алгоритми", "дані"],
    "metadata": {
      "publisher": "MIT Press",
      "publicationYear": 2009
    }
  },
  {
    "id": 2,
    "title": "Чистий код",
    "author": "Роберт Мартін",
    "isAvailable": False,
    "tags": ["програмування", "чистий код"],
    "metadata": {
      "publisher": "Prentice Hall",
      "publicationYear": 2008
    }
  }
]



@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
  for book in books_db:
    if book["id"] == book_id:
      return book
  raise HTTPException(status_code=404, detail="Book not found")



@app.post("/books/", response_model=Book)
async def add_book(book: Book):
  if any(b["id"] == book.id for b in books_db):
    raise HTTPException(status_code=400, detail="Book with this ID already exists")

  books_db.append(book.dict())
  return book



@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
  for book in books_db:
    if book["id"] == book_id:
      books_db.remove(book)
      return {"message": "Book deleted successfully"}

  raise HTTPException(status_code=404, detail="Book not found")



if __name__ == "__main__":
  uvicorn.run("main7_3:app", host="127.0.0.1", reload=True)