from fastapi import FastAPI, UploadFile, File
import os
import uvicorn

app = FastAPI()
UPLOAD_DIRECTORY = "uploaded_images"


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
  os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

  file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
  with open(file_path, "wb") as buffer:
    buffer.write(file.file.read())

  return {"filename": file.filename, "location": file_path}




if __name__ == "__main__":
  uvicorn.run("main15_3:app", host="127.0.0.1", reload=True)