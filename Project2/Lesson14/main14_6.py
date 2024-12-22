from fastapi import FastAPI, BackgroundTasks
import uvicorn
import asyncio
import pytest

app = FastAPI()


async def process_data(data: str):
  await asyncio.sleep(1)
  return f"Оброблено: {data}"


@app.post("/process-data/")
async def process_data_endpoint(background_tasks: BackgroundTasks, data: str):
  background_tasks.add_task(process_data, data)
  return {"message": "Дані відправлені на обробку"}


@pytest.mark.asyncio
async def test_process_data():
  result = await process_data("test")
  assert result == "Оброблено: test"


if __name__ == "__main__":
  uvicorn.run("main14_6:app", host="127.0.0.1", reload=True)
