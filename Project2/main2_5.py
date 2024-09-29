from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()


@app.get("/async-endpoint")
async def read_items():
    await asyncio.sleep(1)
    return {"message": "Асинхронна відповідь після 1 секунди очікування"}


if __name__ == "__main__":
  uvicorn.run("main2_5:app", host="127.0.0.1", reload=True)