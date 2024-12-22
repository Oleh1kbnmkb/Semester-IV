from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from fastapi.testclient import TestClient
import uvicorn
from PIL import Image
import io
import os

app = FastAPI()
UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def resize_image(image_data: bytes, max_size: tuple = (800, 600)) -> bytes:
  try:
    with Image.open(io.BytesIO(image_data)) as img:
      img.thumbnail(max_size)
      img_byte_array = io.BytesIO()
      img.save(img_byte_array, format=img.format)
      return img_byte_array.getvalue()
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")


async def process_image(file_path: str):
  try:
    with open(file_path, "rb") as file:
      resized_image = resize_image(file.read())
    with open(file_path, "wb") as file:
      file.write(resized_image)
  except Exception as e:
    print(f"Error during background processing: {str(e)}")


@app.post("/upload-photo/")
async def upload_photo(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
  file_location = os.path.join(UPLOAD_DIR, file.filename)

  try:
    with open(file_location, "wb") as saved_file:
      saved_file.write(await file.read())

    background_tasks.add_task(process_image, file_location)
    return {"info": "Фотографія завантажена, розпочато обробку.", "filename": file.filename}
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")


@app.get("/download-photo/{filename}")
async def download_photo(filename: str):
  file_path = os.path.join(UPLOAD_DIR, filename)
  if os.path.exists(file_path):
    return FileResponse(file_path)
  raise HTTPException(status_code=404, detail="File not found")


client = TestClient(app)


def test_upload_photo():
  with open("test_files/test_image.jpg", "rb") as file:
    response = client.post(
      "/upload-photo/",
      files={"file": ("test_image.jpg", file, "image/jpeg")}
    )
  assert response.status_code == 200
  assert "Фотографія завантажена, розпочато обробку." in response.json().get("info")


def test_upload_invalid_file_format():
  with open("test_files/test_document.pdf", "rb") as file:
    response = client.post(
      "/upload-photo/",
      files={"file": ("test_document.pdf", file, "application/pdf")}
    )
  assert response.status_code == 400
  assert "Недопустимий формат файлу" in response.json().get("detail")


if __name__ == "__main__":
  uvicorn.run("main15_6:app", host="127.0.0.1", reload=True)
