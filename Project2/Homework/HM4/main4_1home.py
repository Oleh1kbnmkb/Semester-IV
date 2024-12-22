from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks: List[Task] = []


@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Завдання не знайдено")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Завдання не знайдено")


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Завдання не знайдено")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main4_1home:app", host="127.0.0.1", port=8000, reload=True)