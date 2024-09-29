from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI()


def get_book_from_api(title: str):
  url = f"https://openlibrary.org/search.json?title={title}"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    if data['docs']:
      book = data['docs'][0]
      book_key = book.get("key")
      return {
        "title": book.get("title"),
        "author": book.get("author_name", ["Unknown"])[0],
        "publish_year": book.get("first_publish_year"),
        "isbn": book.get("isbn", ["N/A"])[0],
        "link": f"https://openlibrary.org{book_key}"
      }
    else:
      return None
  else:
    return None


@app.get("/book/{title}")
def get_book(title: str):
  book_info = get_book_from_api(title)

  if book_info:
    return {"book": book_info}
  else:
    raise HTTPException(status_code=404, detail="Книга не знайдена або неможливо отримати дані")



if __name__ == "__main__":
  uvicorn.run("main4_8:app", host="127.0.0.1", reload=True)