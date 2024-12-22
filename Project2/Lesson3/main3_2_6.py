from fastapi import FastAPI, HTTPException
import aiomysql
import asyncio
import uvicorn

app = FastAPI()


async def get_db():
    # Use your actual credentials here
    conn = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='your_user', password='your_password',
                                      db='your_database')
    return conn


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    conn = await get_db()
    try:
        async with conn.acquire() as conn:  # Properly acquire connection
            async with conn.cursor() as cur:
                # Use parameterized query to avoid SQL injection
                await cur.execute("SELECT * FROM items WHERE id=%s", (item_id,))
                result = await cur.fetchone()
        if result:
            return {"item_id": item_id, "name": result[1]}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    finally:
        conn.close()


if __name__ == "__main__":
    uvicorn.run("main3_2_6:app", host="127.0.0.1", reload=True)
