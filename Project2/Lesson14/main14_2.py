from fastapi import FastAPI, BackgroundTasks
import asyncio
import uvicorn

app = FastAPI()


async def log_data(data: str):
    await asyncio.sleep(1)
    print(f"Логування даних: {data}")


@app.post("/log-data/")
async def log_data_endpoint(background_tasks: BackgroundTasks, data: str):
    background_tasks.add_task(log_data, data)
    return {"message": "Дані логуються у фоновому режимі"}


@app.get("/")
async def read_root():
    return {"message": "Привіт від FastAPI з фоновими завданнями для логування"}


if __name__ == "__main__":
  uvicorn.run("main14_2:app", host="127.0.0.1", reload=True)