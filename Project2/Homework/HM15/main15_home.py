from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import uvicorn
from typing import List
from pathlib import Path
import aiofiles
import os
from PIL import Image
import asyncio

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_FORMATS = {"image/jpeg", "image/png"}
MAX_FILE_SIZE_MB = 5



def validate_file_size(file: UploadFile):
  file.file.seek(0, os.SEEK_END)
  file_size_mb = file.file.tell() / (1024 * 1024)
  file.file.seek(0)
  if file_size_mb > MAX_FILE_SIZE_MB:
    raise HTTPException(status_code=400, detail="File size exceeds the limit of 5 MB.")



def validate_file_type(file: UploadFile):
  if file.content_type not in ALLOWED_FORMATS:
    raise HTTPException(status_code=400, detail="Unsupported file type. Only JPG and PNG are allowed.")



async def optimize_image(file_path: Path):
  try:
    async with aiofiles.open(file_path, 'rb') as f:
      img = Image.open(f)
      optimized_path = file_path.with_suffix(".optimized.jpg")
      img = img.convert("RGB")
      img.save(optimized_path, format="JPEG", quality=85)
    return True
  except Exception as e:
    print(f"Error optimizing image: {e}")
    return False



@app.post("/upload/")
async def upload_images(files: List[UploadFile], background_tasks: BackgroundTasks):
  uploaded_files = []

  for file in files:
    validate_file_type(file)
    validate_file_size(file)

    file_path = UPLOAD_DIR / file.filename

    async with aiofiles.open(file_path, 'wb') as out_file:
      while content := await file.read(1024 * 1024):
        await out_file.write(content)
    uploaded_files.append(str(file_path))
    background_tasks.add_task(optimize_image, file_path)
  return JSONResponse(content={"message": "Files uploaded successfully.", "files": uploaded_files})



@app.get("/status/")
async def status():
  return {"status": "API is running!"}


def test_file_upload():
  from fastapi.testclient import TestClient
  client = TestClient(app)

  with open("test.jpg", "rb") as test_file:
    response = client.post(
      "/upload/", files={"files": ("test.jpg", test_file, "image/jpeg")}
    )
    assert response.status_code == 200, response.text
    print(response.json())


if __name__ == "__main__":
  uvicorn.run("main15_home:app", host="127.0.0.1", reload=True)
