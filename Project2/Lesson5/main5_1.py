from fastapi import FastAPI, Query, HTTPException
import uvicorn

app = FastAPI()

items_db = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
    {"id": 5, "name": "Item 5"},
    {"id": 6, "name": "Item 6"},
    {"id": 7, "name": "Item 7"},
    {"id": 8, "name": "Item 8"},
]


def get_items_from_database(skip: int, limit: int):
    return items_db[skip:skip + limit]


@app.get("/items/")
async def read_items(skip: int = Query(0, title="Пропустити", description="Кількість записів для пропуску"),
                     limit: int = Query(10, title="Ліміт", description="Максимальна кількість записів для видачі")):
    items = get_items_from_database(skip, limit)
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")
    return {"items": items}

if __name__ == "__main__":
    uvicorn.run("main5_1:app", host="127.0.0.1", reload=True)