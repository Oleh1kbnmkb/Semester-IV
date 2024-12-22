from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from PIL import Image
import io

app = FastAPI()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png"}

def validate_and_sanitize_image(file: UploadFile):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Недозволений формат файлу.")

    try:
        image = Image.open(file.file)
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        return buffered.getvalue()
    except Exception:
        raise HTTPException(status_code=400, detail="Неможливо обробити файл.")

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    file_data = validate_and_sanitize_image(file)
    return {"status": "Файл успішно завантажено"}


if __name__ == "__main__":
  uvicorn.run("main15_7:app", host="127.0.0.1", reload=True)