from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = []


@app.post("/add_names/{name}")
async def add_name(name: str):
  if name in users:
    return {"message": "Error"}
  else:
    users.append(name)
    return {"message": f"Ім'я {name} було успішно додано"}


@app.get("/get_names")
async def get_names():
  return {"users": users}


@app.delete("/delete/{name}/")
async def delete_names(name: str):
  if name in users:
    users.remove(name)
    return {"message": f"Ім'я {name} було успішно видалено"}
  else:
    return {"message": "Error: Ім'я не знайдено"}


if __name__ == "__main__":
  uvicorn.run("main2_4home:app", host="127.0.0.1", reload=True)
