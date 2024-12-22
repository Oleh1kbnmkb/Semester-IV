from fastapi import FastAPI, BackgroundTasks, UploadFile, File
import asyncio
import uvicorn

app = FastAPI()


async def process_file(file: UploadFile):
    await asyncio.sleep(3)
    print(f"Файл {file.filename} оброблено")


@app.post("/upload-file/")
async def upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    background_tasks.add_task(process_file, file)
    return {"message": f"Файл {file.filename} завантажується та обробляється у фоні"}


@app.get("/")
async def read_root():
    return {"message": "Привіт від FastAPI з фоновими завданнями для обробки файлів"}



if __name__ == "__main__":
  uvicorn.run("main14_3:app", host="127.0.0.1", reload=True)