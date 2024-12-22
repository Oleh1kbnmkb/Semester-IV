from fastapi import FastAPI, BackgroundTasks
import asyncio
import logging
import uvicorn

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def example_task(name: str):
    try:
        await asyncio.sleep(2)
        if name == "error":
            raise ValueError("Помилкове завдання")
        logger.info(f"Завдання {name} успішно виконано")
    except Exception as e:
        logger.error(f"Помилка у завданні {name}: {e}")
@app.post("/add-task/")
async def add_task(background_tasks: BackgroundTasks, name: str):
    background_tasks.add_task(example_task, name)
    return {"message": f"Завдання {name} додано до фонових завдань"}
@app.get("/")
async def read_root():
    return {"message": "Вітаємо у FastAPI з моніторингом фонових завдань"}


if __name__ == "__main__":
  uvicorn.run("main14_5:app", host="127.0.0.1", reload=True)