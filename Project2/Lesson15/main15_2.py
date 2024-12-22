import os
import uuid
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List
from pathlib import Path
import uvicorn

app = FastAPI()

# Папка для збереження завантажених файлів
UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


@app.post("/create-post/")
async def create_post(
        description: str = Form(...),
        images: List[UploadFile] = File(...)
):
  image_filenames = []


  MAX_FILES = 10
  MAX_FILE_SIZE_MB = 5

  if len(images) > MAX_FILES:
    raise HTTPException(status_code=400, detail=f"Не більше {MAX_FILES} файлів.")

  for image in images:

    if not image.filename.lower().endswith((".jpg", ".jpeg", ".png")):
      raise HTTPException(status_code=400, detail=f"Недопустимий формат файлу: {image.filename}")


    if image.content_type not in ["image/jpeg", "image/png"]:
      raise HTTPException(status_code=400, detail=f"Недопустимий MIME-тип: {image.content_type}")


    contents = await image.read()
    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
      raise HTTPException(status_code=400, detail=f"Файл {image.filename} перевищує {MAX_FILE_SIZE_MB} MB.")


    unique_name = f"{uuid.uuid4()}_{image.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)


    with open(file_path, "wb") as f:
      f.write(contents)

    image_filenames.append(unique_name)

  return {
    "description": description,
    "images": image_filenames
  }


if __name__ == "__main__":
  uvicorn.run("main15_2:app", host="127.0.0.1", reload=True)
