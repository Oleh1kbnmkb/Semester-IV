from fastapi import FastAPI
import time
import uvicorn
import asyncio

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    time.sleep(2)
    return {"message": "Синхронний запит завершений"}

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(2)
    return {"message": "Асинхронний запит завершений"}


if __name__ == "__main__":
  uvicorn.run("main2_7:app", host="127.0.0.1", reload=True)