from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None
    available: int


books = []


@app.get("/books", response_model=List[Book])
def get_books():
    return books


@app.post("/books", response_model=Book, status_code=201)
def add_book(book: Book):
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books.append(book)
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


if __name__ == "__main__":
  uvicorn.run("main7_1home:app", host="127.0.0.1", reload=True)