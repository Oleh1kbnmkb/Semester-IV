from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

# Асинхронна черга завдань
task_queue = asyncio.Queue()

# Обробник черги
async def process_task_queue():
    while True:
        task_name = await task_queue.get()
        try:
            await example_task(task_name)
        except Exception as e:
            print(f"Помилка під час виконання завдання {task_name}: {e}")
        finally:
            task_queue.task_done()

# Приклад завдання
async def example_task(name: str):
    await asyncio.sleep(2)
    print(f"Завдання {name} виконано")

# Подія запуску додатка
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(process_task_queue())

# Маршрут для додавання завдання
@app.post("/add-task/")
async def add_task(name: str):
    await task_queue.put(name)
    return {"message": f"Завдання {name} додано до черги"}

# Головний маршрут
@app.get("/")
async def read_root():
    return {"message": "Вітаємо у FastAPI з асинхронною чергою завдань!"}




if __name__ == "__main__":
  uvicorn.run("main14_4:app", host="127.0.0.1", reload=True)