from fastapi import FastAPI
import uvicorn

app = FastAPI()

names = []

@app.post("/add-name/{name}")
async def add_name(name: str):
    names.append(name)
    return {"message": f"Ім'я {name} було успішно додано"}

@app.get("/get-names")
async def get_names():
    return {"names": names}


if __name__ == "__main__":
  uvicorn.run("main2_6:app", host="127.0.0.1", reload=True)