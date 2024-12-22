from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get("/books/{isbn}/{year}")
async def get_book(
        isbn: str = Path(..., title="The ISBN of the book"),
        year: int = Path(..., ge=1900, le=2023, title="The year of the book publication")
):
  book_data = fetch_book_data(isbn, year)
  if book_data:
    return book_data
  return {"error": "Book not found"}


def fetch_book_data(isbn: str, year: int):
  sample_books = [
    {"isbn": "9780140449136", "year": 1869, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"isbn": "9780061120084", "year": 1960, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"isbn": "9780743273565", "year": 1925, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"isbn": "9780141439600", "year": 1813, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"isbn": "9781501173219", "year": 2017, "title": "The Handmaid's Tale", "author": "Margaret Atwood"}
  ]
  book = next((b for b in sample_books if b["isbn"] == isbn and b["year"] == year), None)
  return book


if __name__ == "__main__":
  uvicorn.run("main5_8:app", host="127.0.0.1", reload=True)
