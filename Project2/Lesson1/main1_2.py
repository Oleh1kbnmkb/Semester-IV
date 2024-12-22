from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def read_root():
    return {"Hello": "World"}


@app.delete("/")
def read_root():
    return {"Hello": "World"}


@app.put("/")
def read_root():
    return {"Hello": "World"}


@app.patch("/")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
  uvicorn.run("main1_2:app", host="127.0.0.1", reload=True)