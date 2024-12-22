from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil
import uvicorn

app = FastAPI()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка завантаження: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main15_1:app", host="127.0.0.1", reload=True)
