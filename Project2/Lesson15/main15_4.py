import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn

app = FastAPI()

MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_FILE_TYPES = ["image/jpeg", "image/png"]


@app.post("/upload-photo/")
async def upload_photo(file: UploadFile = File(...)):
  if file.size > MAX_FILE_SIZE:
    raise HTTPException(status_code=413, detail="Файл занадто великий")
  if file.content_type not in ALLOWED_FILE_TYPES:
    raise HTTPException(status_code=400, detail="Недопустимий формат файлу")

  save_path = f"./uploads/{file.filename}"
  with open(save_path, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  return {"filename": file.filename, "detail": "Файл успішно завантажено"}



if __name__ == "__main__":
  uvicorn.run("main15_4:app", host="127.0.0.1", reload=True)