from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.get("/books/")
def get_books():
    return {"books": books}

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return {"book": book}
    return {"message": "Книгу з таким ID не знайдено."}



if __name__ == "__main__":
  uvicorn.run("main4_2:app", host="127.0.0.1", reload=True)